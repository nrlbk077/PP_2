--search by pattern
CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    WHERE first_name ILIKE '%' || pattern || '%' OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 2 updete or add members
CREATE OR REPLACE PROCEDURE insert_or_update_user(name TEXT, phone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = name) THEN
        UPDATE phonebook SET phone = insert_or_update_user.phone WHERE first_name = name;
    ELSE
        INSERT INTO phonebook (first_name, phone) VALUES (name, phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

-- deleting by num or by name
CREATE OR REPLACE PROCEDURE delete_user_proc(username TEXT, phone_num TEXT)
AS $$
BEGIN
    DELETE FROM phonebook WHERE first_name = username OR phone = phone_num;
END;
$$ LANGUAGE plpgsql;
