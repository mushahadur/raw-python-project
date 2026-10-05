# routes/orders.py

from services.pharmacy import Pharmacy
from layouts.base import render_layout


def get_orders_page(current_user=None):

    if current_user:
        raw_id = current_user.get("id") or current_user.get("_id") or current_user.get("user_id") or ""
        user_id = str(raw_id)
    else:
        user_id = ""

    """Fetches orders, users, and medicines and renders the order management page."""

    pharmacy = Pharmacy()

    # =========================================================
    # 1. Fetch data
    # =========================================================

    orders = pharmacy.db.fetch_orders(user_id)

    customers = pharmacy.db.fetch_customers()
    medicines = pharmacy.db.fetch_medicines()

    # =========================================================
    # 2. Generate Order Table Rows
    # =========================================================

    table_rows = ""

    for o in orders:

        table_rows += f"""
        <tr class="group
                   border-b border-slate-800/80
                   hover:bg-slate-800/40
                   transition-colors">

            <!-- Order ID -->
            <td class="px-4 py-4 text-center whitespace-nowrap">

                <span class="inline-flex
                             items-center
                             justify-center
                             min-w-10
                             h-8
                             px-2
                             rounded-lg
                             bg-slate-800
                             border border-slate-700
                             text-slate-300
                             text-xs
                             font-semibold">

                    #{o[0]}

                </span>

            </td>


            <!-- Customer -->
            <td class="px-4 py-4 whitespace-nowrap">

                <div class="flex items-center gap-3">

                    <div class="w-9 h-9
                                shrink-0
                                rounded-lg
                                bg-blue-500/10
                                border border-blue-500/20
                                flex items-center justify-center">

                        <svg class="w-4 h-4 text-blue-400"
                             fill="none"
                             stroke="currentColor"
                             viewBox="0 0 24 24">

                            <path stroke-linecap="round"
                                  stroke-linejoin="round"
                                  stroke-width="1.8"
                                  d="M16 7a4 4 0 11-8 0
                                     4 4 0 018 0z
                                     M12 14a7 7 0 00-7 7
                                     h14a7 7 0 00-7-7z">
                            </path>

                        </svg>

                    </div>


                    <div>

                        <p class="text-sm
                                  font-medium
                                  text-slate-200">

                            {o[1]}

                        </p>

                        <p class="text-[11px]
                                  text-slate-500">

                            Customer

                        </p>

                    </div>

                </div>

            </td>


            <!-- Medicine -->
            <td class="px-4 py-4 whitespace-nowrap">

                <div class="flex items-center gap-3">

                    <div class="w-9 h-9
                                shrink-0
                                rounded-lg
                                bg-emerald-500/10
                                border border-emerald-500/20
                                flex items-center justify-center">

                        <svg class="w-4 h-4 text-emerald-400"
                             fill="none"
                             stroke="currentColor"
                             viewBox="0 0 24 24">

                            <path stroke-linecap="round"
                                  stroke-linejoin="round"
                                  stroke-width="1.8"
                                  d="M19.428 15.341
                                     A8 8 0 016.829 6.829
                                     m12.599 8.512
                                     A8 8 0 016.829 6.829
                                     M12 3v18
                                     M3 12h18">
                            </path>

                        </svg>

                    </div>


                    <span class="text-sm text-slate-300">

                        {o[2]}

                    </span>

                </div>

            </td>


            <!-- Quantity -->
            <td class="px-4 py-4
                       text-center
                       whitespace-nowrap">

                <span class="inline-flex
                             items-center
                             justify-center
                             min-w-10
                             px-2.5
                             py-1.5
                             rounded-md
                             bg-blue-500/10
                             border border-blue-500/20
                             text-blue-400
                             text-xs
                             font-semibold">

                    {o[3]}

                </span>

            </td>


            <!-- Total -->
            <td class="px-4 py-4
                       text-right
                       whitespace-nowrap">

                <span class="text-sm
                             font-semibold
                             text-emerald-400">

                    {o[4]}

                </span>

            </td>

        </tr>
        """


    # =========================================================
    # 3. Empty State
    # =========================================================

    if not orders:

        table_rows = """
        <tr>

            <td colspan="5"
                class="px-6 py-16 text-center">

                <div class="flex
                            flex-col
                            items-center
                            justify-center">

                    <div class="w-16 h-16
                                mb-4
                                rounded-2xl
                                bg-slate-800
                                border border-slate-700
                                flex items-center
                                justify-center">

                        <svg class="w-8 h-8 text-slate-500"
                             fill="none"
                             stroke="currentColor"
                             viewBox="0 0 24 24">

                            <path stroke-linecap="round"
                                  stroke-linejoin="round"
                                  stroke-width="1.5"
                                  d="M9 14h6
                                     M9 17h6
                                     M9 10h6
                                     M5 4h14
                                     a1 1 0 011 1v14
                                     a1 1 0 01-1 1H5
                                     a1 1 0 01-1-1V5
                                     a1 1 0 011-1z">
                            </path>

                        </svg>

                    </div>


                    <h3 class="text-base
                               font-semibold
                               text-slate-300">

                        No Orders Found

                    </h3>


                    <p class="mt-1
                              text-sm
                              text-slate-500">

                        Create your first order
                        to see it here.

                    </p>

                </div>

            </td>

        </tr>
        """


    # =========================================================
    # 4. Generate User Dropdown Options
    # =========================================================

    customer_options = ""

    for u in customers:

        customer_options += f"""
        <option value="{u[0]}">
            {u[1]} (ID: {u[0]})
        </option>
        """


    # =========================================================
    # 5. Generate Medicine Dropdown Options
    # =========================================================

    medicine_options = ""

    for m in medicines:

        stock_info = f" — Stock: {m[3]}" if len(m) > 3 else ""

        medicine_options += f"""
        <option value="{m[0]}">
            {m[1]}{stock_info}
        </option>
        """

    # user_id = current_user.get("id", "User")
   

    # =========================================================
    # 6. Page Content
    # =========================================================

    content = f"""

    <!-- =====================================================
         PAGE HEADER
    ====================================================== -->

    <div class="flex
                flex-col
                gap-4
                sm:flex-row
                sm:items-center
                sm:justify-between
                py-6">

        <div>

            <!-- Breadcrumb -->

            <div class="flex
                        items-center
                        gap-2
                        mb-2
                        text-xs
                        text-slate-500">

                <span>
                    Dashboard
                </span>

                <svg class="w-3 h-3"
                     fill="none"
                     stroke="currentColor"
                     viewBox="0 0 24 24">

                    <path stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M9 5l7 7-7 7">
                    </path>

                </svg>

                <span class="text-slate-400">
                    Orders
                </span>

            </div>


            <!-- Title -->

            <h1 class="text-2xl
                       font-bold
                       text-slate-100">

                Order Management

            </h1>


            <p class="mt-1
                      text-sm
                      text-slate-500">

                Manage customer orders
                and medicine sales.

            </p>

        </div>


        <!-- Place Order Button -->

        <button
            type="button"
            onclick="openOrderModal()"
            class="inline-flex
                   items-center
                   justify-center
                   gap-2
                   w-full
                   sm:w-auto
                   px-5
                   py-2.5
                   rounded-lg
                   bg-amber-400
                   hover:bg-amber-300
                   text-slate-950
                   text-sm
                   font-semibold
                   shadow-lg
                   shadow-amber-500/10
                   transition-all
                   focus:outline-none
                   focus:ring-2
                   focus:ring-amber-400/40">

            <svg class="w-4 h-4"
                 fill="none"
                 stroke="currentColor"
                 viewBox="0 0 24 24">

                <path stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M12 4v16
                         M4 12h16">
                </path>

            </svg>

            Place New Order

        </button>

    </div>


    <!-- =====================================================
         ORDERS TABLE
    ====================================================== -->

    <div class="rounded-xl
                border border-slate-800
                bg-slate-900/60
                overflow-hidden
                shadow-xl">


        <!-- Table Header -->

        <div class="px-5
                    py-4
                    border-b border-slate-800
                    flex
                    flex-col
                    sm:flex-row
                    sm:items-center
                    sm:justify-between
                    gap-2">

            <div>

                <h2 class="text-sm
                           font-semibold
                           text-slate-200">

                    All Orders

                </h2>

                <p class="text-xs
                          text-slate-500
                          mt-1">

                    Customer order history
                    and sales details

                </p>

            </div>


            <span class="text-xs
                         text-slate-500">

                {len(orders)} order(s)

            </span>

        </div>


        <!-- Responsive Table -->

        <div class="overflow-x-auto">

            <table class="w-full
                          min-w-[700px]
                          border-collapse
                          text-sm">

                <thead>

                    <tr class="bg-slate-800/50
                               border-b
                               border-slate-800">


                        <!-- Order ID -->

                        <th class="px-4
                                   py-3.5
                                   text-center
                                   text-[11px]
                                   uppercase
                                   tracking-wider
                                   font-semibold
                                   text-slate-500
                                   whitespace-nowrap">

                            Order ID

                        </th>


                        <!-- Customer -->

                        <th class="px-4
                                   py-3.5
                                   text-left
                                   text-[11px]
                                   uppercase
                                   tracking-wider
                                   font-semibold
                                   text-slate-500
                                   whitespace-nowrap">

                            Customer

                        </th>


                        <!-- Medicine -->

                        <th class="px-4
                                   py-3.5
                                   text-left
                                   text-[11px]
                                   uppercase
                                   tracking-wider
                                   font-semibold
                                   text-slate-500
                                   whitespace-nowrap">

                            Medicine

                        </th>


                        <!-- Quantity -->

                        <th class="px-4
                                   py-3.5
                                   text-center
                                   text-[11px]
                                   uppercase
                                   tracking-wider
                                   font-semibold
                                   text-slate-500
                                   whitespace-nowrap">

                            Quantity

                        </th>


                        <!-- Total -->

                        <th class="px-4
                                   py-3.5
                                   text-right
                                   text-[11px]
                                   uppercase
                                   tracking-wider
                                   font-semibold
                                   text-slate-500
                                   whitespace-nowrap">

                            Total

                        </th>

                    </tr>

                </thead>


                <tbody>

                    {table_rows}

                </tbody>

            </table>

        </div>

    </div>


    <!-- =====================================================
         ORDER MODAL
    ====================================================== -->

    <div
        id="orderModal"
        class="hidden
               fixed
               inset-0
               z-[100]
               items-center
               justify-center
               p-4
               bg-slate-950/80
               backdrop-blur-sm">


        <!-- Modal -->

        <div
            class="w-full
                   max-w-lg
                   max-h-[90vh]
                   overflow-y-auto
                   rounded-2xl
                   border border-slate-700
                   bg-slate-900
                   shadow-2xl">


            <!-- Modal Header -->

            <div class="sticky
                        top-0
                        z-10
                        bg-slate-900
                        border-b border-slate-800
                        px-5
                        py-4
                        flex
                        items-center
                        justify-between">


                <div>

                    <h3 class="text-base
                               font-semibold
                               text-slate-100">

                        Place New Order

                    </h3>

                    <p class="text-xs
                              text-slate-500
                              mt-1">

                        Create a new medicine sale

                    </p>

                </div>


                <!-- Close Button -->

                <button
                    type="button"
                    onclick="closeOrderModal()"
                    class="w-9
                           h-9
                           rounded-lg
                           border border-slate-700
                           bg-slate-800
                           text-slate-400
                           hover:text-white
                           hover:bg-slate-700
                           transition-colors
                           flex
                           items-center
                           justify-center
                           focus:outline-none">

                    <svg class="w-5 h-5"
                         fill="none"
                         stroke="currentColor"
                         viewBox="0 0 24 24">

                        <path stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M6 18L18 6
                                 M6 6l12 12">
                        </path>

                    </svg>

                </button>

            </div>


            <!-- =================================================
                 ORDER FORM
            ================================================== -->

            <form
                method="POST"
                action="/place-order"
                class="p-5 space-y-5">


                <!-- Customer   -->

               <input type="hidden" name="user_id" value="{user_id}" class="bg-[#222] text-slate-300 text-sm px-2 py-1 rounded border border-[#444]" readonly />

                 <!-- Customer -->
                
                                <div>
                                
                
                                    <label
                                        for="order_customer_id"
                                        class="block
                                               mb-2
                                               text-xs
                                               font-medium
                                               text-slate-400">
                
                                        Select Customer
                
                                    </label>
                
                
                                    <select
                                        id="order_customer_id"
                                        name="customer_id"
                                        required
                                        class="w-full
                                               px-3
                                               py-2.5
                                               rounded-lg
                                               bg-slate-800
                                               border border-slate-700
                                               text-slate-200
                                               text-sm
                                               focus:outline-none
                                               focus:border-amber-400
                                               focus:ring-2
                                               focus:ring-amber-400/10
                                               transition-colors">
                
                                        <option
                                            value=""
                                            disabled
                                            selected>
                
                                            -- Choose a Customer --
                
                                        </option>
                
                                        {customer_options}
                
                                    </select>
                
                                </div>

                <!-- Medicine -->

                <div>

                    <label
                        for="order_medicine_id"
                        class="block
                               mb-2
                               text-xs
                               font-medium
                               text-slate-400">

                        Select Medicine

                    </label>


                    <select
                        id="order_medicine_id"
                        name="medicine_id"
                        required
                        class="w-full
                               px-3
                               py-2.5
                               rounded-lg
                               bg-slate-800
                               border border-slate-700
                               text-slate-200
                               text-sm
                               focus:outline-none
                               focus:border-amber-400
                               focus:ring-2
                               focus:ring-amber-400/10
                               transition-colors">

                        <option
                            value=""
                            disabled
                            selected>

                            -- Choose a Medicine --

                        </option>

                        {medicine_options}

                    </select>

                </div>


                <!-- Quantity -->

                <div>

                    <label
                        for="order_quantity"
                        class="block
                               mb-2
                               text-xs
                               font-medium
                               text-slate-400">

                        Quantity

                    </label>


                    <input
                        id="order_quantity"
                        type="number"
                        name="quantity"
                        min="1"
                        placeholder="Enter purchase quantity"
                        required
                        class="w-full
                               px-3
                               py-2.5
                               rounded-lg
                               bg-slate-800
                               border border-slate-700
                               text-slate-200
                               text-sm
                               placeholder:text-slate-600
                               focus:outline-none
                               focus:border-amber-400
                               focus:ring-2
                               focus:ring-amber-400/10
                               transition-colors">

                </div>


                <!-- Submit Button -->

                <button
                    type="submit"
                    class="w-full
                           inline-flex
                           items-center
                           justify-center
                           gap-2
                           px-4
                           py-3
                           rounded-lg
                           bg-amber-400
                           hover:bg-amber-300
                           text-slate-950
                           text-sm
                           font-semibold
                           shadow-lg
                           shadow-amber-500/10
                           transition-all
                           focus:outline-none
                           focus:ring-2
                           focus:ring-amber-400/40">

                    <svg class="w-4 h-4"
                         fill="none"
                         stroke="currentColor"
                         viewBox="0 0 24 24">

                        <path stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 5v14
                                 M5 12h14">
                        </path>

                    </svg>

                    Submit Order

                </button>

            </form>

        </div>

    </div>


    <!-- =====================================================
         MODAL JAVASCRIPT
    ====================================================== -->

    <script>

        function openOrderModal() {{

            const modal =
                document.getElementById('orderModal');

            if (!modal) return;

            modal.classList.remove('hidden');
            modal.classList.add('flex');

            document.body.classList.add('overflow-hidden');
        }}


        function closeOrderModal() {{

            const modal =
                document.getElementById('orderModal');

            if (!modal) return;

            modal.classList.add('hidden');
            modal.classList.remove('flex');

            document.body.classList.remove('overflow-hidden');
        }}


        // Close when clicking outside modal

        document
            .getElementById('orderModal')
            ?.addEventListener(
                'click',
                function(event) {{

                    if (event.target === this) {{
                        closeOrderModal();
                    }}

                }}
            );


        // Close with Escape key

        document.addEventListener(
            'keydown',
            function(event) {{

                if (event.key === 'Escape') {{
                    closeOrderModal();
                }}

            }}
        );

    </script>

    """

    return render_layout("Orders", content, current_user)