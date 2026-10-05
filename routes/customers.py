
# routes/customers.py

from services.pharmacy import Pharmacy
from layouts.base import render_layout


def get_customers_page(current_user=None):
    """
    Customer management page.

    Features:
    - Professional responsive UI
    - Mobile-friendly horizontal table
    - User statistics cards
    - Status badges
    - Responsive add-user modal
    - Tailwind CSS
    """

    pharmacy = Pharmacy()
    customers = pharmacy.db.fetch_customers()


    # ============================================================
    # USER STATISTICS
    # ============================================================

    total_users = len(customers)

    active_users = sum(
        1
        for u in customers
        if u[5] == 1
    )

    inactive_users = sum(
        1
        for u in customers
        if u[5] != 1
    )


    # ============================================================
    # GENERATE TABLE ROWS
    # ============================================================

    table_rows = ""

    for u in customers:

        user_id = u[0]
        name = u[1]
        phone = u[2]
        email = u[3]
        address = u[4]
        status = u[5]

        # -----------------------------------------
        # Status Badge
        # -----------------------------------------

        if status == 1:

            status_badge = """
                <span class="
                    inline-flex
                    items-center
                    gap-1.5

                    px-2.5
                    py-1

                    rounded-full

                    text-xs
                    font-semibold

                    bg-emerald-500/10
                    text-emerald-400

                    border
                    border-emerald-500/20
                ">
                    <span class="
                        w-1.5
                        h-1.5
                        rounded-full
                        bg-emerald-400
                    "></span>

                    Active
                </span>
            """

        else:

            status_badge = """
                <span class="
                    inline-flex
                    items-center
                    gap-1.5

                    px-2.5
                    py-1

                    rounded-full

                    text-xs
                    font-semibold

                    bg-red-500/10
                    text-red-400

                    border
                    border-red-500/20
                ">
                    <span class="
                        w-1.5
                        h-1.5
                        rounded-full
                        bg-red-400
                    "></span>

                    Inactive
                </span>
            """


        # -----------------------------------------
        # Table Row
        # -----------------------------------------

        table_rows += f"""
        <tr class="
            group
            border-b
            border-slate-800

            hover:bg-slate-800/50

            transition-colors
            duration-150
        ">

            <!-- User ID -->

            <td class="
                px-4
                py-4

                text-center
                whitespace-nowrap

                text-sm
                font-medium
                text-slate-400
            ">
                #{user_id}
            </td>


            <!-- User -->

            <td class="
                px-4
                py-4
                whitespace-nowrap
            ">

                <div class="
                    flex
                    items-center
                    gap-3
                ">

                    <!-- Avatar -->

                    <div class="
                        flex-shrink-0

                        w-9
                        h-9

                        rounded-lg

                        bg-blue-500/10
                        border
                        border-blue-500/20

                        flex
                        items-center
                        justify-center

                        text-sm
                        font-bold
                        text-blue-400
                    ">
                        {str(name)[0].upper() if name else "U"}
                    </div>


                    <!-- Name -->

                    <div>

                        <p class="
                            text-sm
                            font-semibold
                            text-white
                        ">
                            {name}
                        </p>

                        <p class="
                            text-xs
                            text-slate-500
                            mt-0.5
                        ">
                            User #{user_id}
                        </p>

                    </div>

                </div>

            </td>


            <!-- Phone -->

            <td class="
                px-4
                py-4

                text-center
                whitespace-nowrap

                text-sm
                text-slate-300
            ">

                <div class="
                    inline-flex
                    items-center
                    gap-2
                ">

                    <svg
                        class="w-4 h-4 text-slate-500"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.129a11.042 11.042 0 005.516 5.516l1.129-2.257a1 1 0 011.21-.502l4.493 1.498A1 1 0 0121 15.72V19a2 2 0 01-2 2h-1C9.163 21 3 14.837 3 7V5z"
                        />
                    </svg>

                    <span>
                        {phone}
                    </span>

                </div>

            </td>

             <!-- Email -->
            
            <td class="
                px-4
                py-4

                text-center
                whitespace-nowrap

                text-sm
                text-slate-300
            ">

                <div class="
                    inline-flex
                    items-center
                    gap-2
                ">

                    <svg
                        class="w-4 h-4 text-slate-500"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.129a11.042 11.042 0 005.516 5.516l1.129-2.257a1 1 0 011.21-.502l4.493 1.498A1 1 0 0121 15.72V19a2 2 0 01-2 2h-1C9.163 21 3 14.837 3 7V5z"
                        />
                    </svg>

                    <span>
                        {email}
                    </span>

                </div>

            </td>

            <!-- Address -->
                        
            <td class="
                px-4
                py-4

                text-center
                whitespace-nowrap

                text-sm
                text-slate-300
            ">

                <div class="
                    inline-flex
                    items-center
                    gap-2
                ">

                    <svg
                        class="w-4 h-4 text-slate-500"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.129a11.042 11.042 0 005.516 5.516l1.129-2.257a1 1 0 011.21-.502l4.493 1.498A1 1 0 0121 15.72V19a2 2 0 01-2 2h-1C9.163 21 3 14.837 3 7V5z"
                        />
                    </svg>

                    <span>
                        {address}
                    </span>

                </div>

            </td>

            <!-- Status -->

            <td class="
                px-4
                py-4

                text-center
                whitespace-nowrap
            ">
                {status_badge}
            </td>

        </tr>
        """


    # ============================================================
    # EMPTY STATE
    # ============================================================

    if not customers:

        table_rows = """
        <tr>

            <td
                colspan="4"
                class="px-6 py-16 text-center"
            >

                <div class="
                    flex
                    flex-col
                    items-center
                    justify-center
                ">

                    <div class="
                        w-16
                        h-16

                        rounded-2xl

                        bg-slate-800
                        border
                        border-slate-700

                        flex
                        items-center
                        justify-center

                        text-3xl

                        mb-4
                    ">
                        👥
                    </div>


                    <h3 class="
                        text-base
                        font-semibold
                        text-slate-200
                        mb-1
                    ">
                        No customers found
                    </h3>


                    <p class="
                        text-sm
                        text-slate-500
                        max-w-sm
                    ">
                        There are currently no customers
                        in the system.
                        Add your first user to get started.
                    </p>

                </div>

            </td>

        </tr>
        """


    # ============================================================
    # PAGE CONTENT
    # ============================================================

    content = f"""

    <!-- ========================================================
         PAGE HEADER
    ========================================================= -->

    <div class="
        flex
        flex-col
        gap-4

        sm:flex-row
        sm:items-center
        sm:justify-between

        mb-6
    ">


        <!-- Page Information -->

        <div>

            <div class="
                flex
                items-center
                gap-2

                text-xs
                text-slate-500

                mb-2
            ">

                <span>
                    Management
                </span>

                <span>
                    ›
                </span>

                <span class="text-slate-400">
                    Customers
                </span>

            </div>


            <div class="
                flex
                items-center
                gap-3
            ">

                <div class="
                    w-10
                    h-10

                    rounded-xl

                    bg-blue-500/10
                    border
                    border-blue-500/20

                    flex
                    items-center
                    justify-center

                    text-xl
                ">
                    👥
                </div>


                <div>

                    <h2 class="
                        text-xl
                        sm:text-2xl

                        font-bold

                        text-white

                        tracking-tight
                    ">
                        Customers Management
                    </h2>


                    <p class="
                        text-xs
                        sm:text-sm

                        text-slate-500

                        mt-0.5
                    ">
                        Manage pharmacy system Customers
                    </p>

                </div>

            </div>

        </div>


        <!-- Add User -->

        <button
            type="button"
            onclick="openUserModal()"

            class="
                inline-flex
                items-center
                justify-center
                gap-2

                w-full
                sm:w-auto

                px-4
                py-2.5

                rounded-lg

                bg-blue-600
                hover:bg-blue-500
                active:bg-blue-700

                text-white

                text-sm
                font-semibold

                shadow-lg
                shadow-blue-600/10

                focus:outline-none
                focus:ring-2
                focus:ring-blue-500/40

                transition-all
                duration-200
            "
        >

            <svg
                class="w-4 h-4"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 4v16m8-8H4"
                />
            </svg>

            <span>
                Add Customer
            </span>

        </button>

    </div>


    <!-- ========================================================
         USER STATISTICS
    ========================================================= -->

    <div class="
        grid
        grid-cols-1
        sm:grid-cols-3

        gap-4

        mb-6
    ">


        <!-- Total Users -->

        <div class="
            rounded-xl

            border
            border-slate-800

            bg-slate-900/60

            p-4

            hover:border-slate-700

            transition
        ">

            <div class="
                flex
                items-center
                justify-between
            ">

                <div>

                    <p class="
                        text-xs
                        uppercase
                        tracking-wider
                        text-slate-500
                    ">
                        Total Users
                    </p>


                    <p class="
                        text-2xl
                        font-bold
                        text-white
                        mt-1
                    ">
                        {total_users}
                    </p>

                </div>


                <div class="
                    w-10
                    h-10

                    rounded-lg

                    bg-blue-500/10
                    border
                    border-blue-500/20

                    flex
                    items-center
                    justify-center

                    text-lg
                ">
                    👥
                </div>

            </div>

        </div>


        <!-- Active Users -->

        <div class="
            rounded-xl

            border
            border-slate-800

            bg-slate-900/60

            p-4

            hover:border-slate-700

            transition
        ">

            <div class="
                flex
                items-center
                justify-between
            ">

                <div>

                    <p class="
                        text-xs
                        uppercase
                        tracking-wider
                        text-slate-500
                    ">
                        Active Users
                    </p>


                    <p class="
                        text-2xl
                        font-bold
                        text-emerald-400
                        mt-1
                    ">
                        {active_users}
                    </p>

                </div>


                <div class="
                    w-10
                    h-10

                    rounded-lg

                    bg-emerald-500/10
                    border
                    border-emerald-500/20

                    flex
                    items-center
                    justify-center

                    text-lg
                ">
                    ✓
                </div>

            </div>

        </div>


        <!-- Inactive Users -->

        <div class="
            rounded-xl

            border
            border-slate-800

            bg-slate-900/60

            p-4

            hover:border-slate-700

            transition
        ">

            <div class="
                flex
                items-center
                justify-between
            ">

                <div>

                    <p class="
                        text-xs
                        uppercase
                        tracking-wider
                        text-slate-500
                    ">
                        Inactive Users
                    </p>


                    <p class="
                        text-2xl
                        font-bold
                        text-red-400
                        mt-1
                    ">
                        {inactive_users}
                    </p>

                </div>


                <div class="
                    w-10
                    h-10

                    rounded-lg

                    bg-red-500/10
                    border
                    border-red-500/20

                    flex
                    items-center
                    justify-center

                    text-lg
                ">
                    !
                </div>

            </div>

        </div>

    </div>


    <!-- ========================================================
         USERS TABLE
    ========================================================= -->

    <div class="
        rounded-xl

        border
        border-slate-800

        bg-slate-900/60

        overflow-hidden
    ">


        <!-- Table Header -->

        <div class="
            px-4
            sm:px-5

            py-4

            border-b
            border-slate-800

            flex
            flex-col

            sm:flex-row
            sm:items-center
            sm:justify-between

            gap-2
        ">

            <div>

                <h3 class="
                    text-sm
                    font-semibold
                    text-white
                ">
                    Customers
                </h3>


                <p class="
                    text-xs
                    text-slate-500
                    mt-0.5
                ">
                    Registered pharmacy Customers
                </p>

            </div>


            <span class="
                inline-flex
                w-fit

                items-center

                px-2.5
                py-1

                rounded-full

                bg-slate-800

                text-xs
                text-slate-400
            ">
                {total_users} Records
            </span>

        </div>


        <!--
            Responsive table wrapper.

            On mobile:
            User can scroll horizontally.
        -->

        <div class="overflow-x-auto">

            <table class="
                w-full
                min-w-[650px]

                border-collapse

                text-sm
            ">


                <!-- Table Head -->

                <thead>

                    <tr class="
                        bg-slate-950/70

                        border-b
                        border-slate-800
                    ">

                        <th class="
                            px-4
                            py-3.5

                            text-center

                            text-[11px]
                            uppercase
                            tracking-wider

                            font-semibold

                            text-slate-500

                            whitespace-nowrap
                        ">
                            User ID
                        </th>


                        <th class="
                            px-4
                            py-3.5

                            text-left

                            text-[11px]
                            uppercase
                            tracking-wider

                            font-semibold

                            text-slate-500

                            whitespace-nowrap
                        ">
                            Customer
                        </th>


                        <th class="
                            px-4
                            py-3.5

                            text-center

                            text-[11px]
                            uppercase
                            tracking-wider

                            font-semibold

                            text-slate-500

                            whitespace-nowrap
                        ">
                            Phone
                        </th>

                         <th class="
                                px-4
                                py-3.5
    
                                text-center
    
                                text-[11px]
                                uppercase
                                tracking-wider
    
                                font-semibold
    
                                text-slate-500
    
                                whitespace-nowrap
                            ">
                                Email
                            </th>
                            <th class="
                            px-4
                            py-3.5

                            text-center

                            text-[11px]
                            uppercase
                            tracking-wider

                            font-semibold

                            text-slate-500

                            whitespace-nowrap
                        ">
                            Address
                        </th>


                        <th class="
                            px-4
                            py-3.5

                            text-center

                            text-[11px]
                            uppercase
                            tracking-wider

                            font-semibold

                            text-slate-500

                            whitespace-nowrap
                        ">
                            Status
                        </th>

                    </tr>

                </thead>


                <!-- Table Body -->

                <tbody>

                    {table_rows}

                </tbody>

            </table>

        </div>

    </div>


    <!-- ========================================================
         ADD USER MODAL
    ========================================================= -->

    <div
        id="customerModal"

        class="
            hidden

            fixed
            inset-0

            z-[100]

            items-center
            justify-center

            p-4

            bg-slate-950/80
            backdrop-blur-sm
        "

        role="dialog"
        aria-modal="true"
        aria-labelledby="userModalTitle"
    >


        <!-- Modal Container -->

        <div
            class="
                relative

                w-full
                max-w-lg

                max-h-[90vh]

                overflow-y-auto

                rounded-2xl

                border
                border-slate-700

                bg-slate-900

                shadow-2xl
            "
        >


            <!-- Modal Header -->

            <div class="
                sticky
                top-0
                z-10

                px-5
                sm:px-6

                py-4

                border-b
                border-slate-800

                bg-slate-900/95

                backdrop-blur
            ">

                <div class="
                    flex
                    items-center
                    justify-between
                ">


                    <!-- Header -->

                    <div class="
                        flex
                        items-center
                        gap-3
                    ">

                        <div class="
                            w-10
                            h-10

                            rounded-lg

                            bg-blue-500/10
                            border
                            border-blue-500/20

                            flex
                            items-center
                            justify-center

                            text-lg
                        ">
                            👤
                        </div>


                        <div>

                            <h3
                                id="userModalTitle"

                                class="
                                    text-base
                                    font-bold
                                    text-white
                                "
                            >
                                Add New User
                            </h3>


                            <p class="
                                text-xs
                                text-slate-500
                                mt-0.5
                            ">
                                Enter user information
                            </p>

                        </div>

                    </div>


                    <!-- Close Button -->

                    <button
                        type="button"
                        onclick="closeUserModal()"

                        class="
                            w-9
                            h-9

                            rounded-lg

                            flex
                            items-center
                            justify-center

                            text-slate-400

                            hover:text-white
                            hover:bg-slate-800

                            transition
                        "

                        aria-label="Close modal"
                    >

                        <svg
                            class="w-5 h-5"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                        >

                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M6 18L18 6M6 6l12 12"
                            />

                        </svg>

                    </button>

                </div>

            </div>


            <!-- =================================================
                 FORM
            ================================================== -->

            <form
                method="POST"
                action="/add-customer"

                class="
                    p-5
                    sm:p-6

                    space-y-5
                "
            >


                <!-- User Name -->

                <div>

                    <label
                        for="user_name"

                        class="
                            block
                            mb-2

                            text-sm
                            font-medium
                            text-slate-300
                        "
                    >
                        Full Name

                        <span class="text-red-400">
                            *
                        </span>

                    </label>


                    <input
                        id="user_name"

                        type="text"

                        name="name"

                        placeholder="Enter full name"

                        autocomplete="name"

                        required

                        class="
                            w-full

                            px-3.5
                            py-3

                            rounded-lg

                            bg-slate-950

                            border
                            border-slate-700

                            text-sm
                            text-white

                            placeholder-slate-600

                            outline-none

                            focus:border-blue-500

                            focus:ring-2
                            focus:ring-blue-500/10

                            transition
                        "
                    />

                </div>


                <!-- Phone -->

                <div>

                    <label
                        for="user_phone"

                        class="
                            block
                            mb-2

                            text-sm
                            font-medium
                            text-slate-300
                        "
                    >
                        Phone Number

                        <span class="text-red-400">
                            *
                        </span>

                    </label>


                    <input
                        id="user_phone"

                        type="tel"

                        name="phone"

                        placeholder="Enter phone number"

                        autocomplete="tel"

                        required

                        class="
                            w-full

                            px-3.5
                            py-3

                            rounded-lg

                            bg-slate-950

                            border
                            border-slate-700

                            text-sm
                            text-white

                            placeholder-slate-600

                            outline-none

                            focus:border-blue-500

                            focus:ring-2
                            focus:ring-blue-500/10

                            transition
                        "
                    />

                </div>


                <!-- Email -->
                
                <div>

                    <label
                        for="user_email"

                        class="
                            block
                            mb-2

                            text-sm
                            font-medium
                            text-slate-300
                        "
                    >
                        Email

                        <span class="text-red-400">
                            *
                        </span>

                    </label>


                    <input
                        id="user_email"

                        type="email"

                        name="email"

                        placeholder="Enter email number"

                        autocomplete="email"

                        required

                        class="
                            w-full

                            px-3.5
                            py-3

                            rounded-lg

                            bg-slate-950

                            border
                            border-slate-700

                            text-sm
                            text-white

                            placeholder-slate-600

                            outline-none

                            focus:border-blue-500

                            focus:ring-2
                            focus:ring-blue-500/10

                            transition
                        "
                    />

                </div>

                

                <!-- Address -->
                
                <div>

                    <label
                        for="user_address"

                        class="
                            block
                            mb-2

                            text-sm
                            font-medium
                            text-slate-300
                        "
                    >
                        Address

                        <span class="text-red-400">
                            *
                        </span>

                    </label>


                    <input
                        id="user_address"

                        type="text"

                        name="address"

                        placeholder="Enter address number"

                        autocomplete="tel"

                        required

                        class="
                            w-full

                            px-3.5
                            py-3

                            rounded-lg

                            bg-slate-950

                            border
                            border-slate-700

                            text-sm
                            text-white

                            placeholder-slate-600

                            outline-none

                            focus:border-blue-500

                            focus:ring-2
                            focus:ring-blue-500/10

                            transition
                        "
                    />

                </div>
                                

                <!-- Status -->

                <div>

                    <label
                        for="user_status"

                        class="
                            block
                            mb-2

                            text-sm
                            font-medium
                            text-slate-300
                        "
                    >
                        Account Status
                    </label>


                    <select
                        id="user_status"

                        name="status"

                        class="
                            w-full

                            px-3.5
                            py-3

                            rounded-lg

                            bg-slate-950

                            border
                            border-slate-700

                            text-sm
                            text-white

                            outline-none

                            focus:border-blue-500

                            focus:ring-2
                            focus:ring-blue-500/10

                            transition
                        "
                    >

                        <option value="1">
                            Active
                        </option>

                        <option value="0">
                            Inactive
                        </option>

                    </select>

                </div>


                <!-- Buttons -->

                <div class="
                    flex
                    flex-col-reverse

                    sm:flex-row
                    sm:justify-end

                    gap-3

                    pt-2
                ">


                    <!-- Cancel -->

                    <button
                        type="button"

                        onclick="closeUserModal()"

                        class="
                            w-full
                            sm:w-auto

                            px-5
                            py-2.5

                            rounded-lg

                            border
                            border-slate-700

                            bg-slate-800

                            hover:bg-slate-700

                            text-sm
                            font-semibold

                            text-slate-300
                            hover:text-white

                            transition
                        "
                    >
                        Cancel
                    </button>


                    <!-- Save -->

                    <button
                        type="submit"

                        class="
                            w-full
                            sm:w-auto

                            inline-flex
                            items-center
                            justify-center
                            gap-2

                            px-5
                            py-2.5

                            rounded-lg

                            bg-blue-600

                            hover:bg-blue-500

                            text-white

                            text-sm
                            font-semibold

                            shadow-lg
                            shadow-blue-600/10

                            transition
                        "
                    >

                        <svg
                            class="w-4 h-4"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                        >

                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M5 13l4 4L19 7"
                            />

                        </svg>

                        Save User

                    </button>

                </div>

            </form>

        </div>

    </div>


    <!-- ========================================================
         MODAL JAVASCRIPT
    ========================================================= -->

    <script>

        function openUserModal() {{

            const modal =
                document.getElementById("customerModal");

            modal.classList.remove("hidden");

            modal.classList.add("flex");

            document.body.classList.add("overflow-hidden");


            setTimeout(function() {{

                document
                    .getElementById("user_name")
                    .focus();

            }}, 100);

        }}


        function closeUserModal() {{

            const modal =
                document.getElementById("customerModal");

            modal.classList.add("hidden");

            modal.classList.remove("flex");

            document.body.classList.remove("overflow-hidden");

        }}


        /*
         * Close modal by clicking backdrop
         */

        document
            .getElementById("customerModal")
            .addEventListener(
                "click",
                function(event) {{

                    if (event.target === this) {{

                        closeUserModal();

                    }}

                }}
            );


        /*
         * Close modal with ESC
         */

        document.addEventListener(
            "keydown",
            function(event) {{

                const modal =
                    document.getElementById("customerModal");

                if (
                    event.key === "Escape" &&
                    !modal.classList.contains("hidden")
                ) {{

                    closeUserModal();

                }}

            }}
        );

    </script>

    """

    return render_layout("Customer-List", content, current_user)
