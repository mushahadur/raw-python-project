# routes/register.py

from layouts.base import render_layout


def get_register_page(error=""):

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

                <div class="text-center mb-7">

                    <div class="
                        mx-auto
                        w-14 h-14
                        rounded-2xl
                        bg-[#28a745]/10
                        border border-[#28a745]/20
                        flex items-center justify-center
                        mb-4
                    ">
                        <svg
                            class="w-7 h-7 text-[#28a745]"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="1.8"
                                d="M18 9v6m3-3h-6
                                   M15 7a4 4 0 10-8 0
                                   M3 21a6 6 0 0112 0"
                            />
                        </svg>
                    </div>

                    <h1 class="text-2xl font-bold text-white">
                        Create Account
                    </h1>

                    <p class="text-sm text-slate-500 mt-2">
                        Register a new pharmacy user
                    </p>

                </div>

                {error_html}

                <form
                    method="POST"
                    action="/register"
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
                            minlength="3"
                            autocomplete="username"
                            placeholder="Choose a username"
                            class="
                                w-full
                                px-4 py-3
                                bg-[#181818]
                                border border-[#333]
                                rounded-xl
                                text-white
                                placeholder:text-slate-600
                                focus:outline-none
                                focus:border-[#28a745]
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
                            minlength="3"
                            autocomplete="new-password"
                            placeholder="Create a password"
                            class="
                                w-full
                                px-4 py-3
                                bg-[#181818]
                                border border-[#333]
                                rounded-xl
                                text-white
                                placeholder:text-slate-600
                                focus:outline-none
                                focus:border-[#28a745]
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
                            Confirm Password
                        </label>

                        <input
                            type="password"
                            name="confirm_password"
                            required
                            minlength="3"
                            autocomplete="new-password"
                            placeholder="Confirm your password"
                            class="
                                w-full
                                px-4 py-3
                                bg-[#181818]
                                border border-[#333]
                                rounded-xl
                                text-white
                                placeholder:text-slate-600
                                focus:outline-none
                                focus:border-[#28a745]
                            "
                        >

                    </div>


                    <button
                        type="submit"
                        class="
                            w-full
                            py-3
                            rounded-xl
                            bg-[#28a745]
                            hover:bg-[#218838]
                            text-white
                            font-bold
                            transition
                            shadow-lg
                        "
                    >
                        Create Account
                    </button>

                </form>


                <div class="
                    mt-6
                    pt-5
                    border-t border-[#2d2d2d]
                    text-center
                ">

                    <p class="text-sm text-slate-500">

                        Already have an account?

                        <a
                            href="/login"
                            class="text-[#0088cc] hover:underline font-semibold"
                        >
                            Login
                        </a>

                    </p>

                </div>

            </div>

        </div>

    </div>
    """

    return render_layout("Register", content)