# routes/home.py

from services.pharmacy import Pharmacy
from layouts.base import render_layout

def get_home_page(current_user=None):

    """Generates the dynamic pharmacy dashboard with responsive Tailwind CSS."""

    pharmacy = Pharmacy()

    # ---------------------------------------------------------
    # Dashboard Statistics
    # ---------------------------------------------------------

    # Total Orders
    try:
        total_orders = pharmacy.db.count_orders()
    except AttributeError:
        try:
            total_orders = len(pharmacy.db.fetch_orders())
        except Exception:
            total_orders = 0

    # Total Users
    try:
        total_users = pharmacy.db.count_users()
    except AttributeError:
        try:
            total_users = len(pharmacy.db.fetch_users())
        except Exception:
            total_users = 0

    # Total Medicines
    try:
        total_medicines = pharmacy.db.count_medicines()
    except AttributeError:
        try:
            total_medicines = len(pharmacy.db.fetch_medicines())
        except Exception:
            total_medicines = 0

    # ---------------------------------------------------------
    # Dashboard Content
    # ---------------------------------------------------------

    content = f"""
    <!-- =====================================================
         Dashboard Header
    ====================================================== -->
    <div class="mb-8">

        <!-- Breadcrumb -->
        <div class="flex items-center gap-2 text-xs text-slate-500 mb-3">
            <span>Dashboard</span>
            <span>/</span>
            <span class="text-slate-400">Overview</span>
        </div>

        <div class="flex flex-col sm:flex-row sm:items-end sm:justify-between gap-3">

            <div>
                <h1 class="text-2xl sm:text-3xl font-bold text-white tracking-tight">
                    Welcome to Dashboard
                </h1>

                <p class="text-sm text-slate-400 mt-2">
                    Real-time overview of your Pharmacy Management System.
                </p>
            </div>

            <!-- System Status -->
            <div class="inline-flex items-center gap-2
                        w-fit
                        px-3 py-2
                        rounded-lg
                        bg-[#18251d]
                        border border-[#29452f]">

                <span class="relative flex h-2.5 w-2.5">
                    <span class="animate-ping absolute inline-flex h-full w-full
                                 rounded-full bg-green-400 opacity-60"></span>

                    <span class="relative inline-flex rounded-full
                                 h-2.5 w-2.5 bg-green-500"></span>
                </span>

                <span class="text-xs font-medium text-green-400">
                    System Online
                </span>
            </div>

        </div>
    </div>


    <!-- =====================================================
         KPI Cards
    ====================================================== -->

    <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-5 mb-8">


        <!-- Total Orders -->
        <div class="
            group
            relative
            overflow-hidden
            bg-[#1e1e1e]
            border border-[#2d2d2d]
            rounded-2xl
            p-5
            shadow-lg
            hover:border-[#ffc107]/50
            hover:-translate-y-0.5
            transition-all duration-300
        ">

            <!-- Decorative Background -->
            <div class="
                absolute
                -right-8
                -top-8
                w-28
                h-28
                rounded-full
                bg-[#ffc107]/5
                group-hover:bg-[#ffc107]/10
                transition-all
            "></div>

            <div class="relative">

                <div class="flex items-start justify-between">

                    <!-- Icon -->
                    <div class="
                        w-11
                        h-11
                        rounded-xl
                        bg-[#ffc107]/10
                        border border-[#ffc107]/20
                        flex items-center justify-center
                    ">
                        <svg
                            class="w-5 h-5 text-[#ffc107]"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="1.8"
                                d="M9 14l6-6m-5-4h6a2 2 0 012 2v14a2 2 0 01-2 2H8a2 2 0 01-2-2V6a2 2 0 012-2h2m0 0V2m0 0h4m-4 0h4"
                            />
                        </svg>
                    </div>

                    <!-- Badge -->
                    <span class="
                        text-[10px]
                        font-semibold
                        uppercase
                        tracking-wider
                        text-[#ffc107]
                        bg-[#ffc107]/10
                        px-2.5
                        py-1
                        rounded-full
                    ">
                        Orders
                    </span>

                </div>

                <div class="mt-5">

                    <p class="
                        text-xs
                        text-slate-500
                        uppercase
                        tracking-wider
                        font-semibold
                    ">
                        Total Orders
                    </p>

                    <h2 class="
                        mt-1
                        text-3xl
                        font-bold
                        text-[#ffc107]
                    ">
                        {total_orders}
                    </h2>

                    <p class="mt-2 text-xs text-slate-500">
                        All orders recorded in the system
                    </p>

                </div>

            </div>
        </div>


        <!-- =================================================
             Total Users
        ================================================== -->

        <div class="
            group
            relative
            overflow-hidden
            bg-[#1e1e1e]
            border border-[#2d2d2d]
            rounded-2xl
            p-5
            shadow-lg
            hover:border-[#0088cc]/50
            hover:-translate-y-0.5
            transition-all duration-300
        ">

            <div class="
                absolute
                -right-8
                -top-8
                w-28
                h-28
                rounded-full
                bg-[#0088cc]/5
                group-hover:bg-[#0088cc]/10
                transition-all
            "></div>

            <div class="relative">

                <div class="flex items-start justify-between">

                    <!-- Icon -->
                    <div class="
                        w-11
                        h-11
                        rounded-xl
                        bg-[#0088cc]/10
                        border border-[#0088cc]/20
                        flex items-center justify-center
                    ">
                        <svg
                            class="w-5 h-5 text-[#0088cc]"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="1.8"
                                d="M17 20h5v-2a4 4 0 00-4-4h-1m-4 6H6a4 4 0 01-4-4v-1a4 4 0 014-4h8a4 4 0 014 4v1a4 4 0 01-4 4zM9 9a4 4 0 100-8 4 4 0 000 8zm8 1a3 3 0 100-6"
                            />
                        </svg>
                    </div>

                    <span class="
                        text-[10px]
                        font-semibold
                        uppercase
                        tracking-wider
                        text-[#0088cc]
                        bg-[#0088cc]/10
                        px-2.5
                        py-1
                        rounded-full
                    ">
                        Users
                    </span>

                </div>

                <div class="mt-5">

                    <p class="
                        text-xs
                        text-slate-500
                        uppercase
                        tracking-wider
                        font-semibold
                    ">
                        Employees / Users
                    </p>

                    <h2 class="
                        mt-1
                        text-3xl
                        font-bold
                        text-[#0088cc]
                    ">
                        {total_users}
                    </h2>

                    <p class="mt-2 text-xs text-slate-500">
                        Registered users in the system
                    </p>

                </div>

            </div>
        </div>


        <!-- =================================================
             Total Medicines
        ================================================== -->

        <div class="
            group
            relative
            overflow-hidden
            bg-[#1e1e1e]
            border border-[#2d2d2d]
            rounded-2xl
            p-5
            shadow-lg
            hover:border-[#28a745]/50
            hover:-translate-y-0.5
            transition-all duration-300
            sm:col-span-2
            xl:col-span-1
        ">

            <div class="
                absolute
                -right-8
                -top-8
                w-28
                h-28
                rounded-full
                bg-[#28a745]/5
                group-hover:bg-[#28a745]/10
                transition-all
            "></div>

            <div class="relative">

                <div class="flex items-start justify-between">

                    <!-- Icon -->
                    <div class="
                        w-11
                        h-11
                        rounded-xl
                        bg-[#28a745]/10
                        border border-[#28a745]/20
                        flex items-center justify-center
                    ">
                        <svg
                            class="w-5 h-5 text-[#28a745]"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="1.8"
                                d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M8 5l8 4"
                            />
                        </svg>
                    </div>

                    <span class="
                        text-[10px]
                        font-semibold
                        uppercase
                        tracking-wider
                        text-[#28a745]
                        bg-[#28a745]/10
                        px-2.5
                        py-1
                        rounded-full
                    ">
                        Inventory
                    </span>

                </div>

                <div class="mt-5">

                    <p class="
                        text-xs
                        text-slate-500
                        uppercase
                        tracking-wider
                        font-semibold
                    ">
                        Stock Medicines
                    </p>

                    <h2 class="
                        mt-1
                        text-3xl
                        font-bold
                        text-[#28a745]
                    ">
                        {total_medicines}
                    </h2>

                    <p class="mt-2 text-xs text-slate-500">
                        Medicines available in inventory
                    </p>

                </div>

            </div>
        </div>

    </div>


    <!-- =====================================================
         Quick Overview Section
    ====================================================== -->

    <div class="
        bg-[#1e1e1e]
        border border-[#2d2d2d]
        rounded-2xl
        p-5 sm:p-6
        shadow-lg
    ">

        <div class="
            flex
            flex-col
            sm:flex-row
            sm:items-center
            sm:justify-between
            gap-3
            mb-5
        ">

            <div>
                <h2 class="text-base font-bold text-white">
                    Quick Overview
                </h2>

                <p class="text-xs text-slate-500 mt-1">
                    Current system resource summary
                </p>
            </div>

            <span class="
                text-xs
                text-slate-400
                bg-[#252525]
                border border-[#333]
                px-3
                py-1.5
                rounded-lg
                w-fit
            ">
                Live Data
            </span>

        </div>


        <!-- Overview Rows -->

        <div class="space-y-3">

            <!-- Orders -->
            <div class="
                flex
                items-center
                justify-between
                gap-4
                p-3.5
                bg-[#181818]
                border border-[#2a2a2a]
                rounded-xl
                hover:bg-[#222]
                transition-colors
            ">

                <div class="flex items-center gap-3 min-w-0">

                    <div class="
                        w-9
                        h-9
                        shrink-0
                        rounded-lg
                        bg-[#ffc107]/10
                        flex
                        items-center
                        justify-center
                    ">
                        <svg
                            class="w-4 h-4 text-[#ffc107]"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="1.8"
                                d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h6l5 5v11a2 2 0 01-2 2z"
                            />
                        </svg>
                    </div>

                    <span class="text-sm text-slate-300 truncate">
                        Total Orders
                    </span>

                </div>

                <span class="
                    text-sm
                    font-bold
                    text-[#ffc107]
                    shrink-0
                ">
                    {total_orders}
                </span>

            </div>


            <!-- Users -->
            <div class="
                flex
                items-center
                justify-between
                gap-4
                p-3.5
                bg-[#181818]
                border border-[#2a2a2a]
                rounded-xl
                hover:bg-[#222]
                transition-colors
            ">

                <div class="flex items-center gap-3 min-w-0">

                    <div class="
                        w-9
                        h-9
                        shrink-0
                        rounded-lg
                        bg-[#0088cc]/10
                        flex
                        items-center
                        justify-center
                    ">
                        <svg
                            class="w-4 h-4 text-[#0088cc]"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="1.8"
                                d="M16 21v-2a4 4 0 00-4-4H6a4 4 0 00-4 4v2m8-8a4 4 0 100-8 4 4 0 000 8zm6-3a4 4 0 00-3-3.87M22 21v-2a4 4 0 00-3-3.87"
                            />
                        </svg>
                    </div>

                    <span class="text-sm text-slate-300 truncate">
                        Employees / Users
                    </span>

                </div>

                <span class="
                    text-sm
                    font-bold
                    text-[#0088cc]
                    shrink-0
                ">
                    {total_users}
                </span>

            </div>


            <!-- Medicines -->
            <div class="
                flex
                items-center
                justify-between
                gap-4
                p-3.5
                bg-[#181818]
                border border-[#2a2a2a]
                rounded-xl
                hover:bg-[#222]
                transition-colors
            ">

                <div class="flex items-center gap-3 min-w-0">

                    <div class="
                        w-9
                        h-9
                        shrink-0
                        rounded-lg
                        bg-[#28a745]/10
                        flex
                        items-center
                        justify-center
                    ">
                        <svg
                            class="w-4 h-4 text-[#28a745]"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="1.8"
                                d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M8 5l-4-2"
                            />
                        </svg>
                    </div>

                    <span class="text-sm text-slate-300 truncate">
                        Stock Medicines
                    </span>

                </div>

                <span class="
                    text-sm
                    font-bold
                    text-[#28a745]
                    shrink-0
                ">
                    {total_medicines}
                </span>

            </div>

        </div>

    </div>
    """

    return render_layout("Home", content, current_user)