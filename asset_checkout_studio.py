"""
Asset Checkout Studio
---------------------
Main file for Asset Checkout Manager.
"""

from asset_checkout_manager import AssetCheckoutManager


class AssetCheckoutStudio:

    def __init__(self):

        self.manager = AssetCheckoutManager()

    # ----------------------------------
    # Add Asset
    # ----------------------------------
    def add_asset(self):

        print("\n========== ADD ASSET ==========\n")

        asset_id = input(
            "Asset ID: "
        ).strip()

        asset_name = input(
            "Asset Name: "
        ).strip()

        category = input(
            "Category: "
        ).strip()

        asset = self.manager.add_asset(
            asset_id,
            asset_name,
            category
        )

        if asset:

            print("\nAsset Added Successfully.")

            self.manager.display_asset(asset)

        else:

            print("\nAsset ID already exists.")

    # ----------------------------------
    # Checkout Asset
    # ----------------------------------
    def checkout_asset(self):

        asset_id = input(
            "\nAsset ID: "
        ).strip()

        employee = input(
            "Employee Name: "
        ).strip()

        if self.manager.checkout_asset(
            asset_id,
            employee
        ):

            print("\nAsset checked out successfully.")

        else:

            print("\nCheckout failed.")

    # ----------------------------------
    # Return Asset
    # ----------------------------------
    def return_asset(self):

        asset_id = input(
            "\nAsset ID: "
        ).strip()

        if self.manager.return_asset(
            asset_id
        ):

            print("\nAsset returned successfully.")

        else:

            print("\nReturn failed.")

    # ----------------------------------
    # Mark Lost
    # ----------------------------------
    def mark_lost(self):

        asset_id = input(
            "\nAsset ID: "
        ).strip()

        if self.manager.mark_lost(
            asset_id
        ):

            print("\nAsset marked as lost.")

        else:

            print("\nAsset not found.")

    # ----------------------------------
    # View Assets
    # ----------------------------------
    def view_assets(self):

        self.manager.display_assets()

    # ----------------------------------
    # Summary
    # ----------------------------------
    def summary(self):

        self.manager.display_summary()

    # ----------------------------------
    # Menu
    # ----------------------------------
    def menu(self):

        while True:

            print("\n" + "=" * 55)
            print("         ASSET CHECKOUT MANAGER")
            print("=" * 55)

            print("1. Add Asset")
            print("2. Checkout Asset")
            print("3. Return Asset")
            print("4. Mark Asset Lost")
            print("5. View Assets")
            print("6. Summary")
            print("7. Exit")

            choice = input(
                "\nEnter Choice: "
            ).strip()

            if choice == "1":

                self.add_asset()

            elif choice == "2":

                self.checkout_asset()

            elif choice == "3":

                self.return_asset()

            elif choice == "4":

                self.mark_lost()

            elif choice == "5":

                self.view_assets()

            elif choice == "6":

                self.summary()

            elif choice == "7":

                print(
                    "\nThank you for using Asset Checkout Manager."
                )

                break

            else:

                print("\nInvalid choice.")


# ----------------------------------
# Main
# ----------------------------------

if __name__ == "__main__":

    studio = AssetCheckoutStudio()

    studio.menu()