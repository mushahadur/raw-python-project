# routes/login.py

from layouts.base import render_layout


def get_login_page(error=""):

    error_html = ""

    if error:
        error_html = f"""
        <div class="mb-4 p-3 rounded-lg
                    bg-red-500/10
                    border border-red-500/30
                    text-red-400 text-sm">
            {error}
        </div>
        """

    content = f"""
    <div class="min-h-[500px] flex items-center justify-center py-10">

        <div class="w-full max-w-md">

            <div class="
                bg-[#1e1e1e]
                border border-[#2d2d2d]
                rounded-2xl
                shadow-2xl
                p-6 sm:p-8
            ">

                <!-- Header -->
                <div class="text-center mb-7">

                    <div class="
                        mx-auto
                        w-14 h-14
                        rounded-2xl
                        bg-[#0088cc]/10
                        border border-[#0088cc]/20
                        flex items-center justify-center
                        mb-4
                    ">
                        <svg
                            class="w-7 h-7 text-[#0088cc]"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="1.8"
                                d="M15 3h4a2 2 0 012 2v14a2 2 0 01-2 2h-4
                                   M10 17l5-5-5-5
                                   M15 12H3"
                            />
                        </svg>
                    </div>

                    <h1 class="text-2xl font-bold text-white">
                        Welcome Back
                    </h1>

                    <p class="text-sm text-slate-500 mt-2">
                        Login to Pharmacy Management System
                    </p>

                </div>

                {error_html}

                <!-- Login Form -->
                <form
                    method="POST"
                    action="/login"
                    class="space-y-5"
                >

                    <div>

                        <label class="
                            block
                            text-xs
                            font-semibold
                            text-slate-400
                            mb-2
                        ">
                            Username
                        </label>

                        <input
                            type="text"
                            name="username"
                            required
                            autocomplete="username"
                            placeholder="Enter username"
                            class="
                                w-full
                                px-4 py-3
                                bg-[#181818]
                                border border-[#333]
                                rounded-xl
                                text-white
                                placeholder:text-slate-600
                                focus:outline-none
                                focus:border-[#0088cc]
                                transition
                            "
                        >

                    </div>


                    <div>

                        <label class="
                            block
                            text-xs
                            font-semibold
                            text-slate-400
                            mb-2
                        ">
                            Password
                        </label>

                        <input
                            type="password"
                            name="password"
                            required
                            autocomplete="current-password"
                            placeholder="Enter password"
                            class="
                                w-full
                                px-4 py-3
                                bg-[#181818]
                                border border-[#333]
                                rounded-xl
                                text-white
                                placeholder:text-slate-600
                                focus:outline-none
                                focus:border-[#0088cc]
                                transition
                            "
                        >

                    </div>


                    <button
                        type="submit"
                        class="
                            w-full
                            py-3
                            rounded-xl
                            bg-[#0088cc]
                            hover:bg-[#0077b5]
                            text-white
                            font-bold
                            transition
                            shadow-lg
                        "
                    >
                        Login
                    </button>

                </form>


                <div class="
                    mt-6
                    pt-5
                    border-t border-[#2d2d2d]
                    text-center
                ">

                    <p class="text-sm text-slate-500">

                        Don't have an account?

                        <a
                            href="/register"
                            class="text-[#0088cc] hover:underline font-semibold"
                        >
                            Register
                        </a>

                    </p>

                </div>

            </div>

        </div>

    </div>
    """

    return render_layout("Login", content)