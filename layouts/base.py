# layouts/base.py

from layouts.header import render_header
from layouts.footer import render_footer

def render_layout(title, content, current_user=None):
    header_html = render_header(current_user)
    footer_html = render_footer()

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} | Pharmacy Management System</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-[#121212] text-[#e0e0e0] font-sans antialiased min-h-screen flex flex-col">

        <!-- HEADER -->
        {header_html}

        <!-- MAIN -->
        <main class="w-full max-w-[1200px] mx-auto px-4 sm:px-5 py-6 flex-1">
            {content}
        </main>

        <!-- FOOTER -->
        {footer_html}

        <!-- MOBILE MENU JS -->
        <script>
            const mobileMenuButton = document.getElementById("mobileMenuButton");
            const mobileMenu = document.getElementById("mobileMenu");

            if (mobileMenuButton && mobileMenu) {{
                mobileMenuButton.addEventListener("click", function() {{
                    mobileMenu.classList.toggle("hidden");
                }});
            }}
        </script>

    </body>
    </html>
    """