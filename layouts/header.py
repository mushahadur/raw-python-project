# layouts/header.py

def render_header(current_user=None):
    # ---------------------------------------------------------
    # Authentication UI
    # ---------------------------------------------------------
    if current_user:
        username = current_user.get("username", "User")
        auth_menu = f"""
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 w-full sm:w-auto">
            <div class="flex items-center gap-2 px-3 py-2 bg-[#181818] border border-[#333] rounded-lg">
                <div class="w-7 h-7 rounded-full bg-[#0088cc] flex items-center justify-center text-white text-xs font-bold uppercase">
                    {username[0]}
                </div>
                <span class="text-sm text-slate-300 max-w-[150px] truncate">
                    {username}
                </span>
            </div>
            <a href="/logout" class="inline-flex items-center justify-center gap-2 px-3 py-2 rounded-lg border border-[#3a3a3a] text-slate-400 hover:text-red-400 hover:border-red-500/40 hover:bg-red-500/5 transition">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M15 3h4a2 2 0 012 2v14a2 2 0 01-2 2h-4 M10 17l5-5-5-5 M15 12H3"/>
                </svg>
                <span class="text-sm font-medium">Logout</span>
            </a>
        </div>
        """
    else:
        auth_menu = """
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-2 w-full sm:w-auto">
            <a href="/login" class="px-3 py-2 text-center sm:text-left text-sm text-slate-300 hover:text-white transition">
                Login
            </a>
            <a href="/register" class="px-4 py-2 text-center rounded-lg bg-[#0088cc] hover:bg-[#0077b5] text-white text-sm font-semibold transition">
                Register
            </a>
        </div>
        """

    # ---------------------------------------------------------
    # Main Navigation
    # ---------------------------------------------------------
    if current_user:
        desktop_navigation = """
        <nav class="hidden md:flex items-center gap-1">
            <a href="/home" class="px-3 py-2 rounded-lg text-sm text-slate-300 hover:text-white hover:bg-[#292929] transition">Home</a>
            <a href="/orders" class="px-3 py-2 rounded-lg text-sm text-slate-300 hover:text-white hover:bg-[#292929] transition">Orders</a>
            <a href="/medicine" class="px-3 py-2 rounded-lg text-sm text-slate-300 hover:text-white hover:bg-[#292929] transition">Medicines</a>
            <a href="/customer-list" class="px-3 py-2 rounded-lg text-sm text-slate-300 hover:text-white hover:bg-[#292929] transition">Customer</a>
            <a href="/user-list" class="px-3 py-2 rounded-lg text-sm text-slate-300 hover:text-white hover:bg-[#292929] transition">Users</a>
        </nav>
        """
        mobile_navigation = """
        <nav class="flex flex-col gap-1 w-full">
            <a href="/home" class="px-3 py-2 rounded-lg text-sm text-slate-300 hover:text-white hover:bg-[#292929] transition">Home</a>
            <a href="/orders" class="px-3 py-2 rounded-lg text-sm text-slate-300 hover:text-white hover:bg-[#292929] transition">Orders</a>
            <a href="/medicine" class="px-3 py-2 rounded-lg text-sm text-slate-300 hover:text-white hover:bg-[#292929] transition">Medicines</a>
            <a href="/customer-list" class="px-3 py-2 rounded-lg text-sm text-slate-300 hover:text-white hover:bg-[#292929] transition">Customer</a>
            <a href="/user-list" class="px-3 py-2 rounded-lg text-sm text-slate-300 hover:text-white hover:bg-[#292929] transition">Users</a>
        </nav>
        """
    else:
        desktop_navigation = ""
        mobile_navigation = ""

    # Header HTML Return
    return f"""
    <header class="bg-[#1f1f1f] border-b border-[#2d2d2d] shadow-lg sticky top-0 z-50">
        <div class="max-w-[1200px] mx-auto px-4 sm:px-5">
            <div class="min-h-[64px] flex items-center justify-between gap-4">
                
                <!-- Logo -->
                <a href="/home" class="flex items-center gap-3 shrink-0">
                    <div class="w-9 h-9 rounded-xl flex items-center justify-center shadow-lg">
                        <svg class="w-8 h-8 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6V3z" />
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M6 12h2l1.5-3 1.5 6 1.5-4.5 1 1.5h4.5" />
                        </svg>
                    </div>
                    <div class="hidden sm:block">
                        <div class="text-sm font-bold text-white">Pharmacy</div>
                        <div class="text-[10px] text-slate-500 uppercase tracking-wider">Management System</div>
                    </div>
                </a>

                <!-- Desktop Navigation -->
                {desktop_navigation}

                <!-- Auth Menu (Desktop) -->
                <div class="hidden md:flex">
                    {auth_menu}
                </div>

                <!-- Mobile Button -->
                <button id="mobileMenuButton" type="button" class="md:hidden w-10 h-10 rounded-lg border border-[#333] bg-[#181818] flex items-center justify-center text-slate-300 hover:text-white focus:outline-none">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M4 6h16 M4 12h16 M4 18h16"/>
                    </svg>
                </button>

            </div>

            <!-- Mobile Menu Dropdown (Structured outside the inner flex row to take full width) -->
            <div id="mobileMenu" class="hidden md:hidden border-t border-[#2d2d2d] py-4 space-y-3">
                {mobile_navigation}
                <div class="pt-3 border-t border-[#2d2d2d]">
                    {auth_menu}
                </div>
            </div>

        </div>
    </header>
    """