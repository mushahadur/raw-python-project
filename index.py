# index.py

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

from layouts.base import render_layout
from services.pharmacy import Pharmacy

# Existing routes
from routes.home import get_home_page
from routes.orders import get_orders_page
from routes.users import get_users_page
from routes.customers import get_customers_page
from routes.medicines import get_medicines_page

# Authentication routes
from routes.auth.login import get_login_page
from routes.auth.register import get_register_page
from routes.auth.logout import logout

# Authentication service
from services.auth_service import authenticate_user, create_user

# Middleware
from middleware.auth import (
    require_authentication,
    create_session,
    get_current_user
)

class MyHandler(BaseHTTPRequestHandler):

    # =========================================================
    # Helper: Redirect
    # =========================================================

    def redirect(self, path):

        self.send_response(303)

        self.send_header(
            "Location",
            path
        )

        self.end_headers()


    # =========================================================
    # GET Request
    # =========================================================

    def do_GET(self):

        # -----------------------------------------------------
        # Authentication Middleware
        # -----------------------------------------------------

        if not require_authentication(self):
            return

        current_user = get_current_user(self)
        # -----------------------------------------------------
        # Route
        # -----------------------------------------------------

        path = self.path.split("?")[0]


        # Login
        if path == "/login":

            response = get_login_page()

            self.send_response(200)
            self.send_header(
                "Content-type",
                "text/html; charset=utf-8"
            )
            self.end_headers()

            self.wfile.write(
                response.encode("utf-8")
            )

            return


        # Register
        elif path == "/register":

            response = get_register_page()

            self.send_response(200)
            self.send_header(
                "Content-type",
                "text/html; charset=utf-8"
            )
            self.end_headers()

            self.wfile.write(
                response.encode("utf-8")
            )

            return


        # Home
        elif path == "/home" or path == "/":

            response = get_home_page(current_user)


        # Orders
        elif path == "/orders":

            response = get_orders_page(current_user)


        # Users
        elif path == "/user-list":

            response = get_users_page(current_user)


        # Customers
        elif path == "/customer-list":

            response = get_customers_page(current_user)



        # Medicines
        elif path == "/medicine":

            response = get_medicines_page(current_user)


        # Logout
        elif path == "/logout":

            logout(self)
            return


        # 404
        else:

            response = render_layout(
                "404 Not Found",
                """
                <div class="py-20 text-center">
                    <h1 class="text-4xl font-bold text-white">
                        404
                    </h1>

                    <p class="text-slate-500 mt-2">
                        Page Not Found
                    </p>
                </div>
                """
            )


        # -----------------------------------------------------
        # Send Response
        # -----------------------------------------------------

        self.send_response(200)

        self.send_header(
            "Content-type",
            "text/html; charset=utf-8"
        )

        self.end_headers()

        self.wfile.write(
            response.encode("utf-8")
        )


    # =========================================================
    # POST Request
    # =========================================================

    def do_POST(self):

        # -----------------------------------------------------
        # Read POST body
        # -----------------------------------------------------

        content_length = int(
            self.headers.get("Content-Length", 0)
        )

        post_data = self.rfile.read(
            content_length
        ).decode("utf-8")


        fields = urllib.parse.parse_qs(
            post_data
        )


        # -----------------------------------------------------
        # LOGIN
        # -----------------------------------------------------

        if self.path == "/login":

            username = fields.get(
                "username",
                [""]
            )[0].strip()

            password = fields.get(
                "password",
                [""]
            )[0]


            user = authenticate_user(
                username,
                password
            )


            if user is None:

                response = get_login_page(
                    "Invalid username or password."
                )

                self.send_response(401)

                self.send_header(
                    "Content-type",
                    "text/html; charset=utf-8"
                )

                self.end_headers()

                self.wfile.write(
                    response.encode("utf-8")
                )

                return


            # ---------------------------------------------
            # Create Session
            # ---------------------------------------------

            session_id = create_session(user)


            self.send_response(303)

            self.send_header(
                "Set-Cookie",
                f"session_id={session_id}; "
                "Path=/; "
                "HttpOnly; "
                "SameSite=Lax"
            )

            self.send_header(
                "Location",
                "/home"
            )

            self.end_headers()

            return


        # -----------------------------------------------------
        # REGISTER
        # -----------------------------------------------------

        elif self.path == "/register":

            username = fields.get(
                "username",
                [""]
            )[0].strip()

            password = fields.get(
                "password",
                [""]
            )[0]

            confirm_password = fields.get(
                "confirm_password",
                [""]
            )[0]


            # Validation
            if len(username) < 3:

                response = get_register_page(
                    "Username must be at least 3 characters."
                )

                self.send_response(400)

                self.send_header(
                    "Content-type",
                    "text/html; charset=utf-8"
                )

                self.end_headers()

                self.wfile.write(
                    response.encode("utf-8")
                )

                return


            if len(password) < 3:

                response = get_register_page(
                    "Password must be at least 3 characters."
                )

                self.send_response(400)

                self.send_header(
                    "Content-type",
                    "text/html; charset=utf-8"
                )

                self.end_headers()

                self.wfile.write(
                    response.encode("utf-8")
                )

                return


            if password != confirm_password:

                response = get_register_page(
                    "Passwords do not match."
                )

                self.send_response(400)

                self.send_header(
                    "Content-type",
                    "text/html; charset=utf-8"
                )

                self.end_headers()

                self.wfile.write(
                    response.encode("utf-8")
                )

                return


            # ---------------------------------------------
            # Create User
            # ---------------------------------------------

            created = create_user(
                username,
                password
            )


            if not created:

                response = get_register_page(
                    "Username already exists."
                )

                self.send_response(409)

                self.send_header(
                    "Content-type",
                    "text/html; charset=utf-8"
                )

                self.end_headers()

                self.wfile.write(
                    response.encode("utf-8")
                )

                return


            # Registration successful
            self.redirect("/login")

            return


        # -----------------------------------------------------
        # Existing Protected POST Routes
        # -----------------------------------------------------

        # All POST route authentication
        if not require_authentication(self):
            return

        current_user = get_current_user(self)

        pharmacy = Pharmacy()

        redirect_path = "/home"


        # -----------------------------------------------------
        # Add User
        # -----------------------------------------------------

        if self.path == "/add-user":

            name = fields.get(
                "name",
                [""]
            )[0]

            phone = fields.get(
                "phone",
                [""]
            )[0]

            status = fields.get(
                "status",
                [""]
            )[0]


            pharmacy.add_new_user(
                name,
                phone,
                status
            )

            redirect_path = "/user-list"



        # -----------------------------------------------------
        # Add Customer
        # -----------------------------------------------------

        if self.path == "/add-customer":

            name = fields.get(
                "name",
                [""]
            )[0]

            phone = fields.get(
                "phone",
                [""]
            )[0]

            email = fields.get(
                "email",
                [""]
            )[0]

            address = fields.get(
                "address",
                [""]
            )[0]

            status = fields.get(
                "status",
                [""]
            )[0]


            pharmacy.add_new_customer(
                name,
                phone,
                email,
                address,
                status
            )

            redirect_path = "/customer-list"


        # -----------------------------------------------------
        # Add Medicine
        # -----------------------------------------------------

        elif self.path == "/add-medicine":

            name = fields.get(
                "name",
                [""]
            )[0]

            price = float(
                fields.get(
                    "price",
                    [0]
                )[0]
            )

            stock = int(
                fields.get(
                    "stock",
                    [0]
                )[0]
            )

            status = fields.get(
                "status",
                [""]
            )[0]


            pharmacy.add_new_medicine(
                name,
                price,
                stock,
                status
            )

            redirect_path = "/medicine"


        # -----------------------------------------------------
        # Place Order
        # -----------------------------------------------------

        elif self.path == "/place-order":

            user_id = int(
                fields.get(
                    "user_id",
                    [0]
                )[0]
            )

            customer_id = int(
                        fields.get(
                            "customer_id",
                            [0]
                        )[0]
                    )

            medicine_id = int(
                fields.get(
                    "medicine_id",
                    [0]
                )[0]
            )

            quantity = int(
                fields.get(
                    "quantity",
                    [0]
                )[0]
            )


            pharmacy.place_order(
                user_id,
                customer_id,
                medicine_id,
                quantity
            )

            redirect_path = "/orders"


        # -----------------------------------------------------
        # Unknown POST
        # -----------------------------------------------------

        else:

            redirect_path = "/home"


        # -----------------------------------------------------
        # Redirect
        # -----------------------------------------------------

        self.redirect(redirect_path)


# =============================================================
# Start Server
# =============================================================

if __name__ == "__main__":

    server_address = ("", 8080)

    httpd = HTTPServer(
        server_address,
        MyHandler
    )

    print(
        "Server running on http://localhost:8080"
    )

    httpd.serve_forever()