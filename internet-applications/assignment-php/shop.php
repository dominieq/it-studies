<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>South Park Shop</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" media="screen" href="shop.css">
        <?php
            session_start();
            $db = new mysqli("localhost", "root", "", "shopSQL");
            $result = $db->query("SELECT * FROM products");
            
            if(isset($_POST['add'])) {
                // Obsługa dodania do koszyka
                if(!isset($_SESSION['cart'])) {
                    // Jeśli jeszcze nie ma koszyka
                    $_SESSION['cart'] = [];
                }
                $product_name = $_GET['name'];
                if(!in_array($product_name, $_SESSION['cart'])) {
                    array_push($_SESSION['cart'], $product_name);
                    header('Location: shop.php');
                } else {
                    echo "<script> alert('Produkt znajduje się już w koszyku') </script>";
                    echo "<script> location = 'shop.php' </script>";
                }
            } elseif (isset($_POST['buy'])) {
                // Obsługa kupowania produktów z koszyka
                $db->autocommit(FALSE);
                $db->begin_transaction();
                $stmt = $db->prepare("DELETE FROM `products` WHERE `products`.`Name` = ?");
                $bought = TRUE;
                foreach($_SESSION['cart'] as $elem_to_buy) {
                    printf($elem_to_buy);
                    $stmt->bind_param("s", $elem_to_buy);
                    $stmt->execute();
                    if($db->affected_rows == 0) {
                        // Obsługa współbieżnego dostępu
                        echo "<script> alert(\"Przykro nam ale zabrakło ".$elem_to_buy." w sklepie\") </script>";
                        $bought = FALSE;
                        break; 
                    }
                }
                if($bought) {
                    $db->commit();
                    session_unset();
                    header('Location: shop.php');
                } else {
                    $db->rollback();
                    session_unset();
                    echo "<script> location = 'shop.php' </script>";
                }
            } elseif (isset($_POST['discard'])) {
                // Obsługa wyrzucenia produktów z koszyka
                session_unset();
                header('Location: shop.php');
            }
        ?>
    </head>
    <body>
        <table class="product_table">
            <?php while ($row = $result->fetch_assoc()) { ?>
            <tr class="product">
                <td class="prod_name"><?php echo $row["Name"];?></td>
                <td class="prod_category"><?php echo $row["Category"]; ?></td>
                <td class="prod_price"><?php echo $row["Price"]; ?></td>
                <td class="prod_add_button">
                    <form action="shop.php?action=add&name=<?=$row["Name"]?>" method="POST">
                        <input class="add_button" type="submit" name="add" value="Dodaj do koszyka">
                    </form>
                </td>
            </tr>
            <?php } ?>
        </table>
        <?php 
        if(!empty($_SESSION['cart'])) {
            echo "<table class=\"cart_table\">";
            foreach ($_SESSION['cart'] as $product) {
                echo "<tr class=\"cart_product\"> <td class=\"cart_product_name\">".$product."</td> </tr>";
            }
            echo "<tr class=\"cart_buttons\">";
            // Przycisk do kupienia zawartości koszyka
            echo "<td class=\"cart_buy_button\">";
            echo "<form action=\"shop.php?action=buy\" method=\"POST\">";
            echo "<input class=\"buy_products\" type=\"submit\" name=\"buy\" value=\"Kup produkty\"></form></td>";
            // Przycisk do wyrzucenia zawartości koszyka
            echo "<td class=\"cart_discard_button\">";
            echo "<form action=\"shop.php?action=discard\" method=\"POST\">";
            echo "<input class=\"discard_products\" type=\"submit\" name=\"discard\" value=\"Wyrzuć produkty\"></form></td>";
            echo "</tr></table>";
        } else {
            echo "<div class=\"no_cart\">Brak produktów w koszyku</div>";
        }?>  
    </body>
</html>
