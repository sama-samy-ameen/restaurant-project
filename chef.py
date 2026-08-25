
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





