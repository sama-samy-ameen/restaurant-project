
from restaurant_common_data import Order,global_menu,global_orders

class Chef:
    def __init__(self, name, title="Head Chef"):
        self.name=name
        self.title=title


    def view_pending_orders(self, global_orders):
        print(f"---Kitchen Order Queue ({self.name}-{self.title})---")
        pending_count=0
        for order in global_orders:
            if order.status != "Completed":
                pending_count+=1
                print(f"Order number {order.order_id} - [Table {order.table_number}] - Status: {order.status}")
                for item in order.items:
                    print(f" - {item.item_name}")
        if pending_count==0:
            print ("No active orders at the moment..")

    def update_order_status(self, order_id, new_status, global_orders):
        for order in global_orders:
            if order.order_id==order_id:
                order.status=new_status
                print(f"[Chef] Order number {order.order_id} - Status updates to: {new_status}")
                return
        print("[Chef] Order not found.")

    def change_item_availability(self, item_id, availability, global_menu):
        for item in global_menu:
            if item.item_id==item_id:
                item.availability= availability
                status="Available" if availability else "Out of stock"
                print(f"[Chef] '{item.item_name}' Status updated to: {status} ")
                return
        print("[Chef] Menu item not found")

if __name__ == "__main__":

    # ==========================================
    # Complete Test for Chef Class
    # ==========================================
    print("=== TESTING CHEF CLASS ===")

    # 1. Create Chef instance
    chef1 = Chef("David")

    # 2. Create sample orders & add to global_orders
    sample_order1 = Order(table_number=5, order_id=1)
    sample_order1.items.append(global_menu[0])  # Pizza
    sample_order1.items.append(global_menu[3])  # Juice
    global_orders.append(sample_order1)

    sample_order2 = Order(table_number=2, order_id=2)
    sample_order2.items.append(global_menu[1])  # Pasta
    global_orders.append(sample_order2)

    # ------------------------------------------
    # Test 1: View Pending Orders Queue
    # ------------------------------------------
    print("\n--- TEST 1: View Initial Orders ---")
    chef1.view_pending_orders(global_orders)

    # ------------------------------------------
    # Test 2: Update Order Status
    # ------------------------------------------
    print("\n--- TEST 2: Update Order Status ---")
    chef1.update_order_status(1, "In Progress", global_orders)
    chef1.update_order_status(1, "Ready", global_orders)

    # View queue again to confirm status updated
    print("\n--- Verifying Updated Status ---")
    chef1.view_pending_orders(global_orders)

    # ------------------------------------------
    # Test 3: Change Item Availability (Out of Stock)
    # ------------------------------------------
    print("\n--- TEST 3: Change Availability ---")
    # Mark Pasta (item_id 2) as Out of Stock (False)
    chef1.change_item_availability(2, False, global_menu)

    # Verify Pasta is marked False
    print(f"Pasta Availability in Menu: {global_menu[1].availability}")

    print("\n=== ALL TESTS COMPLETED SUCCESSFULLY ===")
