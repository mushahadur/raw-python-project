
import mysql.connector

class DBConnection:

    def __init__(
        self,
        host="localhost",
        user="root",
        password="mysql@123",
        database="pharmacy_db"
    ):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        self.cursor = self.conn.cursor()


    # =========================================================
    # USERS
    # =========================================================

    def fetch_users(self):
        """
        Fetch all system users
        """

        self.cursor.execute("""
            SELECT
                id,
                username,
                role,
                status
            FROM users
            ORDER BY id ASC
        """)

        return self.cursor.fetchall()


    def fetch_user_by_id(self, user_id):
        """
        ID  user 
        """

        self.cursor.execute("""
            SELECT
                id,
                username,
                password_hash,
                role,
                status
            FROM users
            WHERE id = %s
            LIMIT 1
        """, (user_id,))

        return self.cursor.fetchone()


    def fetch_user_by_username(self, username):
        """
        Username  user 
        """

        self.cursor.execute("""
            SELECT
                id,
                username,
                password_hash,
                role,
                status
            FROM users
            WHERE username = %s
            LIMIT 1
        """, (username,))

        return self.cursor.fetchone()


    def add_user(
        self,
        username,
        password_hash,
        role="staff",
        status=True
    ):
        """
        Create a New system user
        """

        sql = """
            INSERT INTO users
            (
                username,
                password_hash,
                role,
                status
            )
            VALUES (%s, %s, %s, %s)
        """

        values = (
            username,
            password_hash,
            role,
            status
        )

        self.cursor.execute(sql, values)
        self.conn.commit()

        return self.cursor.lastrowid


    def username_exists(self, username):
        """
        Check Username
        """

        self.cursor.execute("""
            SELECT id
            FROM users
            WHERE username = %s
            LIMIT 1
        """, (username,))

        return self.cursor.fetchone() is not None


    # =========================================================
    # CUSTOMERS
    # =========================================================

    def fetch_customers(self):
        """
       Get all customers
        """

        self.cursor.execute("""
            SELECT
                id,
                name,
                phone,
                email,
                address,
                status
            FROM customers
            ORDER BY id ASC
        """)

        return self.cursor.fetchall()


    def fetch_customer(self, customer_id):
        """
        Search by customer ID
        """

        self.cursor.execute("""
            SELECT
                id,
                name,
                phone,
                email,
                address,
                status
            FROM customers
            WHERE id = %s
            LIMIT 1
        """, (customer_id,))

        return self.cursor.fetchone()


    def add_customer(
        self,
        name,
        phone,
        email=None,
        address=None,
        status=True
    ):
        """
        Create a new customer 
        """

        sql = """
            INSERT INTO customers
            (
                name,
                phone,
                email,
                address,
                status
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            name,
            phone,
            email,
            address,
            status
        )

        self.cursor.execute(sql, values)
        self.conn.commit()

        return self.cursor.lastrowid


    # =========================================================
    # MEDICINES
    # =========================================================

    def fetch_medicines(self):

        self.cursor.execute("""
            SELECT
                id,
                name,
                price,
                stock,
                status
            FROM medicines
            ORDER BY id ASC
        """)

        return self.cursor.fetchall()


    def add_medicine(
        self,
        name,
        price,
        stock,
        status=True
    ):

        sql = """
            INSERT INTO medicines
            (
                name,
                price,
                stock,
                status
            )
            VALUES (%s, %s, %s, %s)
        """

        values = (
            name,
            price,
            stock,
            status
        )

        self.cursor.execute(sql, values)
        self.conn.commit()

        return self.cursor.lastrowid


    # =========================================================
    # ORDERS
    # =========================================================

    def place_order(
        self,
        user_id,
        customer_id,
        medicine_id,
        quantity
    ):

        # -----------------------------------------------------
        # Medicine check
        # -----------------------------------------------------

        self.cursor.execute("""
            SELECT
                price,
                stock
            FROM medicines
            WHERE id = %s
              AND status = 1
        """, (medicine_id,))

        result = self.cursor.fetchone()

        if not result:
            return "❌ Medicine not found or inactive"


        price, stock = result


        # -----------------------------------------------------
        # Stock check
        # -----------------------------------------------------

        if stock < quantity:
            return "❌ Not enough stock"


        # -----------------------------------------------------
        # Total price
        # -----------------------------------------------------

        total_price = price * quantity


        # -----------------------------------------------------
        # Insert order
        # -----------------------------------------------------

        sql = """
            INSERT INTO orders
            (
                user_id,
                customer_id,
                medicine_id,
                quantity,
                total_price
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            user_id,
            customer_id,
            medicine_id,
            quantity,
            total_price
        )

        self.cursor.execute(sql, values)


        # -----------------------------------------------------
        # Update medicine stock
        # -----------------------------------------------------

        self.cursor.execute("""
            UPDATE medicines
            SET stock = stock - %s
            WHERE id = %s
        """, (quantity, medicine_id))


        self.conn.commit()


        return (
            f"✅ Order placed successfully! "
            f"Total: {total_price}"
        )


    # =========================================================
    # FETCH ORDERS
    # =========================================================

    def fetch_orders(self, user_id):
        
        query = """
            SELECT 
                o.id,
                c.name AS customer_name,   
                m.name AS medicine_name,  
                o.quantity, 
                o.total_price 
            FROM orders o
            JOIN customers c ON o.customer_id = c.id    
            JOIN medicines m ON o.medicine_id = m.id    
            WHERE o.user_id = %s                       
            ORDER BY o.id ASC
        """
        
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchall()



    # =========================================================
    # SALES REPORT
    # =========================================================

    def sales_report(self):

        # Total orders

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM orders
        """)

        total_orders = self.cursor.fetchone()[0]


        # Total sales

        self.cursor.execute("""
            SELECT SUM(total_price)
            FROM orders
        """)

        total_sales = self.cursor.fetchone()[0] or 0


        # Top medicine

        self.cursor.execute("""
            SELECT
                m.name,
                SUM(o.quantity) AS total_qty

            FROM orders o

            JOIN medicines m
                ON o.medicine_id = m.id

            GROUP BY m.id, m.name

            ORDER BY total_qty DESC

            LIMIT 1
        """)

        top_medicine = self.cursor.fetchone()


        return {
            "total_orders": total_orders,
            "total_sales": total_sales,
            "top_medicine": top_medicine
        }


    # =========================================================
    # CUSTOMER REPORT
    # =========================================================

    def customer_report(self, customer_id):

        # Total orders

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM orders
            WHERE customer_id = %s
        """, (customer_id,))

        total_orders = self.cursor.fetchone()[0]


        # Total spent

        self.cursor.execute("""
            SELECT SUM(total_price)
            FROM orders
            WHERE customer_id = %s
        """, (customer_id,))

        total_spent = self.cursor.fetchone()[0] or 0


        # Purchased medicines

        self.cursor.execute("""
            SELECT
                m.name,
                SUM(o.quantity) AS total_qty

            FROM orders o

            JOIN medicines m
                ON o.medicine_id = m.id

            WHERE o.customer_id = %s

            GROUP BY m.id, m.name

            ORDER BY total_qty DESC
        """, (customer_id,))

        medicines = self.cursor.fetchall()


        return {
            "total_orders": total_orders,
            "total_spent": total_spent,
            "medicines": medicines
        }


    # =========================================================
    # COUNT
    # =========================================================

    def count_orders(self):

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM orders
        """)

        return self.cursor.fetchone()[0]


    def count_users(self):

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM users
        """)

        return self.cursor.fetchone()[0]


    def count_medicines(self):

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM medicines
        """)

        return self.cursor.fetchone()[0]


    def count_customers(self):

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM customers
        """)

        return self.cursor.fetchone()[0]


    # =========================================================
    # CLOSE CONNECTION
    # =========================================================

    def close(self):

        if self.cursor:
            self.cursor.close()

        if self.conn:
            self.conn.close()

