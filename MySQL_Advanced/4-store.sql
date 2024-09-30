-- Create a trigger that decreases the quantity of an item after adding a new order.

DELIMITER //
CREATE TRIGGER update_quantity AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//
DELIMITER ;

-- When an order is placed, this trigger automatically updates the quantity in the items table.
-- No need to worry about keeping things in sync manually, MySQL has your back.
