
# routes/medicines.py

from services.pharmacy import Pharmacy
from layouts.base import render_layout


def get_medicines_page(current_user=None):
    """
    Medicine management page.

    Features:
    - Responsive medicine table
    - Professional dashboard-style UI
    - Mobile-friendly horizontal table scrolling
    - Responsive add-medicine modal
    - Tailwind CSS
    """

    pharmacy = Pharmacy()
    medicines = pharmacy.db.fetch_medicines()

    # ============================================================
    # GENERATE TABLE ROWS
    # ============================================================

    table_rows = ""

    for m in medicines:

        # Status badge
        status = str(m[4])

        if status.lower() == "1":
            status_badge = """
                <span class="
                    inline-flex items-center gap-1.5
                    px-2.5 py-1
                    rounded-full
                    text-xs font-semibold
                    bg-emerald-500/10
                    text-emerald-400
                    border border-emerald-500/20
                ">
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                    Available
                </span>
            """
        else:
            status_badge = """
                <span class="
                    inline-flex items-center gap-1.5
                    px-2.5 py-1
                    rounded-full
                    text-xs font-semibold
                    bg-red-500/10
                    text-red-400
                    border border-red-500/20
                ">
                    <span class="w-1.5 h-1.5 rounded-full bg-red-400"></span>
                    Out of Stock
                </span>
            """

        table_rows += f"""
        <tr class="
            group
            border-b border-slate-800
            hover:bg-slate-800/50
            transition-colors duration-150
        ">

            <!-- Medicine ID -->
            <td class="
                px-4 py-4
                whitespace-nowrap
                text-center
                text-sm
                font-medium
                text-slate-300
            ">
                {m[0]}
            </td>


            <!-- Medicine Name -->
            <td class="
                px-4 py-4
                whitespace-nowrap
                text-sm
                font-medium
                text-white
            ">
                <div class="flex items-center gap-3">

                    <div class="
                        flex-shrink-0
                        w-9 h-9
                        rounded-lg
                        bg-blue-500/10
                        border border-blue-500/20
                        flex items-center justify-center
                        text-lg
                    ">
                        💊
                    </div>

                    <span>
                        {m[1]}
                    </span>

                </div>
            </td>


            <!-- Price -->
            <td class="
                px-4 py-4
                whitespace-nowrap
                text-center
                text-sm
                font-semibold
                text-slate-200
            ">
                <span class="text-slate-500 mr-0.5">
                    ৳
                </span>
                {m[2]}
            </td>


            <!-- Stock -->
            <td class="
                px-4 py-4
                whitespace-nowrap
                text-center
                text-sm
                text-slate-300
            ">
                {m[3]}
            </td>


            <!-- Status -->
            <td class="
                px-4 py-4
                whitespace-nowrap
                text-center
            ">
                {status_badge}
            </td>

        </tr>
        """


    # ============================================================
    # EMPTY STATE
    # ============================================================

    if not medicines:

        table_rows = """
        <tr>
            <td colspan="5" class="px-6 py-16 text-center">

                <div class="flex flex-col items-center justify-center">

                    <div class="
                        w-16 h-16
                        rounded-2xl
                        bg-slate-800
                        border border-slate-700
                        flex items-center justify-center
                        text-3xl
                        mb-4
                    ">
                        💊
                    </div>

                    <h3 class="
                        text-base
                        font-semibold
                        text-slate-200
                        mb-1
                    ">
                        No medicines found
                    </h3>

                    <p class="
                        text-sm
                        text-slate-500
                        max-w-sm
                    ">
                        Your medicine inventory is currently empty.
                        Add your first medicine to get started.
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
        flex flex-col
        gap-4
        sm:flex-row
        sm:items-center
        sm:justify-between
        mb-6
    ">

        <!-- Page Information -->

        <div>

            <div class="
                flex items-center gap-2
                text-xs
                text-slate-500
                mb-2
            ">
                <span>Inventory</span>
                <span>›</span>
                <span class="text-slate-400">
                    Medicines
                </span>
            </div>

            <div class="flex items-center gap-3">

                <div class="
                    w-10 h-10
                    rounded-xl
                    bg-blue-500/10
                    border border-blue-500/20
                    flex items-center justify-center
                    text-xl
                ">
                    💊
                </div>

                <div>

                    <h2 class="
                        text-xl
                        sm:text-2xl
                        font-bold
                        text-white
                        tracking-tight
                    ">
                        Medicine Inventory
                    </h2>

                    <p class="
                        text-xs
                        sm:text-sm
                        text-slate-500
                        mt-0.5
                    ">
                        Manage your pharmacy medicine stock
                    </p>

                </div>

            </div>

        </div>


        <!-- Add Medicine Button -->

        <button
            type="button"
            onclick="openMedicineModal()"
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
                Add Medicine
            </span>

        </button>

    </div>


    <!-- ========================================================
         SUMMARY CARDS (Always 3 Cards in a Row)
    ========================================================= -->

    <div class="
        grid
        grid-cols-3
        gap-3
        mb-6
    ">

        <!-- Total Medicines -->

        <div class="
            rounded-xl
            border border-slate-800
            bg-slate-900/60
            p-3
            hover:border-slate-700
            transition
        ">

            <div class="flex flex-col xs:flex-row items-start xs:items-center justify-between gap-1">

                <div>

                    <p class="
                        text-[10px]
                        sm:text-xs
                        uppercase
                        tracking-wider
                        text-slate-500
                        truncate
                    ">
                        Total Meds
                    </p>

                    <p class="
                        text-xl
                        sm:text-2xl
                        font-bold
                        text-white
                        mt-0.5
                    ">
                        {len(medicines)}
                    </p>

                </div>

                <div class="
                    w-8 h-8
                    sm:w-10 sm:h-10
                    rounded-lg
                    bg-blue-500/10
                    border border-blue-500/20
                    flex items-center justify-center
                    text-base
                    sm:text-lg
                    shrink-0
                ">
                    💊
                </div>

            </div>

        </div>


        <!-- Available -->

        <div class="
            rounded-xl
            border border-slate-800
            bg-slate-900/60
            p-3
            hover:border-slate-700
            transition
        ">

            <div class="flex flex-col xs:flex-row items-start xs:items-center justify-between gap-1">

                <div>

                    <p class="
                        text-[10px]
                        sm:text-xs
                        uppercase
                        tracking-wider
                        text-slate-500
                        truncate
                    ">
                        Available
                    </p>

                    <p class="
                        text-xl
                        sm:text-2xl
                        font-bold
                        text-emerald-400
                        mt-0.5
                    ">
                        {
                            sum(
                                1
                                for m in medicines
                                if str(m[4]).lower() == "1"
                            )
                        }
                    </p>

                </div>

                <div class="
                    w-8 h-8
                    sm:w-10 sm:h-10
                    rounded-lg
                    bg-emerald-500/10
                    border border-emerald-500/20
                    flex items-center justify-center
                    text-base
                    sm:text-lg
                    shrink-0
                ">
                    ✓
                </div>

            </div>

        </div>


        <!-- Out of Stock -->

        <div class="
            rounded-xl
            border border-slate-800
            bg-slate-900/60
            p-3
            hover:border-slate-700
            transition
        ">

            <div class="flex flex-col xs:flex-row items-start xs:items-center justify-between gap-1">

                <div>

                    <p class="
                        text-[10px]
                        sm:text-xs
                        uppercase
                        tracking-wider
                        text-slate-500
                        truncate
                    ">
                        Out of Stock
                    </p>

                    <p class="
                        text-xl
                        sm:text-2xl
                        font-bold
                        text-red-400
                        mt-0.5
                    ">
                        {
                            sum(
                                1
                                for m in medicines
                                if str(m[4]).lower() != "1"
                            )
                        }
                    </p>

                </div>

                <div class="
                    w-8 h-8
                    sm:w-10 sm:h-10
                    rounded-lg
                    bg-red-500/10
                    border border-red-500/20
                    flex items-center justify-center
                    text-base
                    sm:text-lg
                    shrink-0
                ">
                    !
                </div>

            </div>

        </div>

    </div>



    <!-- ========================================================
         MEDICINE TABLE
    ========================================================= -->

    <div class="
        rounded-xl
        border border-slate-800
        bg-slate-900/60
        overflow-hidden
    ">

        <!-- Table Header -->

        <div class="
            px-4
            sm:px-5
            py-4
            border-b border-slate-800
            flex flex-col
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
                    Medicine Stock
                </h3>

                <p class="
                    text-xs
                    text-slate-500
                    mt-0.5
                ">
                    Current medicine inventory
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
                {len(medicines)} Records
            </span>

        </div>


        <!--
            IMPORTANT:
            Horizontal scrolling on small/mobile screens
        -->

        <div class="overflow-x-auto">

            <table class="
                w-full
                min-w-[700px]
                border-collapse
                text-sm
            ">

                <thead>

                    <tr class="
                        bg-slate-950/70
                        border-b border-slate-800
                    ">

                        <th class="
                            px-4 py-3.5
                            text-center
                            text-[11px]
                            uppercase
                            tracking-wider
                            font-semibold
                            text-slate-500
                            whitespace-nowrap
                        ">
                            Medicine ID
                        </th>

                        <th class="
                            px-4 py-3.5
                            text-left
                            text-[11px]
                            uppercase
                            tracking-wider
                            font-semibold
                            text-slate-500
                            whitespace-nowrap
                        ">
                            Medicine
                        </th>

                        <th class="
                            px-4 py-3.5
                            text-center
                            text-[11px]
                            uppercase
                            tracking-wider
                            font-semibold
                            text-slate-500
                            whitespace-nowrap
                        ">
                            Price
                        </th>

                        <th class="
                            px-4 py-3.5
                            text-center
                            text-[11px]
                            uppercase
                            tracking-wider
                            font-semibold
                            text-slate-500
                            whitespace-nowrap
                        ">
                            Stock Qty
                        </th>

                        <th class="
                            px-4 py-3.5
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


                <tbody>
                    {table_rows}
                </tbody>

            </table>

        </div>

    </div>


    <!-- ========================================================
         ADD MEDICINE MODAL
    ========================================================= -->

    <div
        id="medicineModal"
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
        aria-labelledby="medicineModalTitle"
    >

        <!-- Modal -->

        <div
            id="medicineModalContent"
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

                transform
                transition-all
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

                    <div class="flex items-center gap-3">

                        <div class="
                            w-10 h-10
                            rounded-lg
                            bg-blue-500/10
                            border border-blue-500/20
                            flex items-center justify-center
                            text-lg
                        ">
                            💊
                        </div>

                        <div>

                            <h3
                                id="medicineModalTitle"
                                class="
                                    text-base
                                    font-bold
                                    text-white
                                "
                            >
                                Add New Medicine
                            </h3>

                            <p class="
                                text-xs
                                text-slate-500
                                mt-0.5
                            ">
                                Enter medicine information
                            </p>

                        </div>

                    </div>


                    <!-- Close -->

                    <button
                        type="button"
                        onclick="closeMedicineModal()"
                        class="
                            w-9 h-9
                            rounded-lg
                            flex items-center justify-center

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


            <!-- Form -->

            <form
                method="POST"
                action="/add-medicine"
                class="
                    p-5
                    sm:p-6
                    space-y-5
                "
            >

                <!-- Medicine Name -->

                <div>

                    <label
                        for="medicine_name"
                        class="
                            block
                            mb-2
                            text-sm
                            font-medium
                            text-slate-300
                        "
                    >
                        Medicine Name
                        <span class="text-red-400">*</span>
                    </label>

                    <input
                        id="medicine_name"
                        type="text"
                        name="name"
                        placeholder="Enter medicine name"
                        required

                        class="
                            w-full
                            px-3.5
                            py-3

                            rounded-lg

                            bg-slate-950
                            border border-slate-700

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


                <!-- Price -->

                <div>

                    <label
                        for="medicine_price"
                        class="
                            block
                            mb-2
                            text-sm
                            font-medium
                            text-slate-300
                        "
                    >
                        Price
                        <span class="text-red-400">*</span>
                    </label>

                    <div class="relative">

                        <span class="
                            absolute
                            left-3.5
                            top-1/2
                            -translate-y-1/2
                            text-slate-500
                            text-sm
                        ">
                            ৳
                        </span>

                        <input
                            id="medicine_price"
                            type="number"
                            step="0.01"
                            min="0"
                            name="price"
                            placeholder="0.00"
                            required

                            class="
                                w-full
                                pl-8
                                pr-3.5
                                py-3

                                rounded-lg

                                bg-slate-950
                                border border-slate-700

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

                </div>


                <!-- Stock -->

                <div>

                    <label
                        for="medicine_stock"
                        class="
                            block
                            mb-2
                            text-sm
                            font-medium
                            text-slate-300
                        "
                    >
                        Stock Quantity
                        <span class="text-red-400">*</span>
                    </label>

                    <input
                        id="medicine_stock"
                        type="number"
                        min="0"
                        name="stock"
                        placeholder="Enter quantity"
                        required

                        class="
                            w-full
                            px-3.5
                            py-3

                            rounded-lg

                            bg-slate-950
                            border border-slate-700

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
                        for="medicine_status"
                        class="
                            block
                            mb-2
                            text-sm
                            font-medium
                            text-slate-300
                        "
                    >
                        Status
                    </label>

                    <select
                        id="medicine_status"
                        name="status"

                        class="
                            w-full
                            px-3.5
                            py-3

                            rounded-lg

                            bg-slate-950
                            border border-slate-700

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
                            Available
                        </option>

                        <option value="0">
                            Out of Stock
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

                    <button
                        type="button"
                        onclick="closeMedicineModal()"
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

                        Save Medicine

                    </button>

                </div>

            </form>

        </div>

    </div>


    <!-- ========================================================
         MODAL JAVASCRIPT
    ========================================================= -->

    <script>

        function openMedicineModal() {{

            const modal =
                document.getElementById("medicineModal");

            modal.classList.remove("hidden");

            modal.classList.add("flex");

            document.body.classList.add("overflow-hidden");

            setTimeout(function() {{

                document
                    .getElementById("medicine_name")
                    .focus();

            }}, 100);
        }}


        function closeMedicineModal() {{

            const modal =
                document.getElementById("medicineModal");

            modal.classList.add("hidden");

            modal.classList.remove("flex");

            document.body.classList.remove("overflow-hidden");
        }}


        /*
         * Close when clicking backdrop
         */

        document
            .getElementById("medicineModal")
            .addEventListener("click", function(event) {{

                if (event.target === this) {{

                    closeMedicineModal();

                }}

            }});


        /*
         * Close using ESC key
         */

        document.addEventListener("keydown", function(event) {{

            if (
                event.key === "Escape" &&
                !document
                    .getElementById("medicineModal")
                    .classList
                    .contains("hidden")
            ) {{

                closeMedicineModal();

            }}

        }});

    </script>
    """

    return render_layout("Medicine", content, current_user)
