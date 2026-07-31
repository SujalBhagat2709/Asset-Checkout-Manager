"""
Asset Checkout Manager
----------------------
File : asset_checkout_manager.py

Features
--------
✔ Add Asset
✔ Checkout Asset
✔ Return Asset
✔ Lost Asset Tracking
✔ Available Asset List
✔ Assigned Asset List
✔ Asset History
✔ Summary Report
"""


class AssetCheckoutManager:

    def __init__(self):

        self.assets = []

    # ----------------------------------
    # Asset Exists
    # ----------------------------------
    def asset_exists(self,
                     asset_id):

        for asset in self.assets:

            if asset["Asset ID"] == asset_id:

                return True

        return False

    # ----------------------------------
    # Add Asset
    # ----------------------------------
    def add_asset(self,
                  asset_id,
                  asset_name,
                  category):

        if self.asset_exists(asset_id):

            return None

        asset = {

            "Asset ID": asset_id,
            "Asset Name": asset_name,
            "Category": category,
            "Assigned To": "-",
            "Status": "Available",
            "History": ["Asset Added"]

        }

        self.assets.append(asset)

        return asset

    # ----------------------------------
    # Checkout Asset
    # ----------------------------------
    def checkout_asset(self,
                       asset_id,
                       employee):

        for asset in self.assets:

            if asset["Asset ID"] == asset_id:

                if asset["Status"] != "Available":

                    return False

                asset["Assigned To"] = employee

                asset["Status"] = "Checked Out"

                asset["History"].append(
                    f"Checked Out to {employee}"
                )

                return True

        return False

    # ----------------------------------
    # Return Asset
    # ----------------------------------
    def return_asset(self,
                     asset_id):

        for asset in self.assets:

            if asset["Asset ID"] == asset_id:

                if asset["Status"] != "Checked Out":

                    return False

                employee = asset["Assigned To"]

                asset["Assigned To"] = "-"

                asset["Status"] = "Available"

                asset["History"].append(
                    f"Returned by {employee}"
                )

                return True

        return False

    # ----------------------------------
    # Mark Lost
    # ----------------------------------
    def mark_lost(self,
                  asset_id):

        for asset in self.assets:

            if asset["Asset ID"] == asset_id:

                asset["Status"] = "Lost"

                asset["History"].append(
                    "Marked as Lost"
                )

                return True

        return False

    # ----------------------------------
    # Available Assets
    # ----------------------------------
    def available_assets(self):

        return [

            asset

            for asset in self.assets

            if asset["Status"] == "Available"

        ]

    # ----------------------------------
    # Checked Out Assets
    # ----------------------------------
    def assigned_assets(self):

        return [

            asset

            for asset in self.assets

            if asset["Status"] == "Checked Out"

        ]

    # ----------------------------------
    # Summary
    # ----------------------------------
    def summary(self):

        available = len(self.available_assets())

        assigned = len(self.assigned_assets())

        lost = len(

            [

                asset

                for asset in self.assets

                if asset["Status"] == "Lost"

            ]

        )

        return {

            "Total Assets":
                len(self.assets),

            "Available":
                available,

            "Checked Out":
                assigned,

            "Lost":
                lost

        }

    # ----------------------------------
    # Display Asset
    # ----------------------------------
    def display_asset(self,
                      asset):

        print("\n========== ASSET ==========\n")

        print(
            f"Asset ID      : {asset['Asset ID']}"
        )

        print(
            f"Asset Name    : {asset['Asset Name']}"
        )

        print(
            f"Category      : {asset['Category']}"
        )

        print(
            f"Assigned To   : {asset['Assigned To']}"
        )

        print(
            f"Status        : {asset['Status']}"
        )

    # ----------------------------------
    # Display Assets
    # ----------------------------------
    def display_assets(self):

        if not self.assets:

            print("\nNo assets found.")

            return

        print("\n========== ASSET LIST ==========\n")

        for index, asset in enumerate(
                self.assets,
                start=1):

            print(f"Asset {index}")

            print("-" * 40)

            self.display_asset(asset)

            print()

    # ----------------------------------
    # Display Summary
    # ----------------------------------
    def display_summary(self):

        report = self.summary()

        print("\n========== SUMMARY ==========\n")

        for key, value in report.items():

            print(f"{key:<18}: {value}")


# ----------------------------------
# Example
# ----------------------------------

if __name__ == "__main__":

    manager = AssetCheckoutManager()

    while True:

        print("\n1. Add Asset")
        print("2. Checkout Asset")
        print("3. Return Asset")
        print("4. Mark Asset Lost")
        print("5. View Assets")
        print("6. Summary")
        print("7. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            asset = manager.add_asset(

                input("Asset ID: "),

                input("Asset Name: "),

                input("Category: ")

            )

            if asset:

                manager.display_asset(asset)

            else:

                print("\nAsset ID already exists.")

        elif choice == "2":

            if manager.checkout_asset(

                input("Asset ID: "),

                input("Employee Name: ")

            ):

                print("\nAsset checked out successfully.")

            else:

                print("\nCheckout failed.")

        elif choice == "3":

            if manager.return_asset(

                input("Asset ID: ")

            ):

                print("\nAsset returned successfully.")

            else:

                print("\nReturn failed.")

        elif choice == "4":

            if manager.mark_lost(

                input("Asset ID: ")

            ):

                print("\nAsset marked as lost.")

            else:

                print("\nAsset not found.")

        elif choice == "5":

            manager.display_assets()

        elif choice == "6":

            manager.display_summary()

        elif choice == "7":

            print(
                "\nThank you for using Asset Checkout Manager."
            )

            break

        else:

            print("\nInvalid choice.")