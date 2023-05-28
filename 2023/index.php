<!DOCTYPE html>
<html>
<head>
    <title>SS</title>
<style>
h1 {
  color: green;
font-family: Arial, sans-serif;
font-size: 50px;
  font-weight: 1000;
}
		body {
			background-color: #f1f1f1; 
			color: #333; 
		}
	</style>
</head>
<body>
<?php
$host = "localhost"; 
$port = "5432";
$dbname = "shop";
$user = "postgres"; 
$password = "root"; 
$conn = pg_connect("host=$host port=$port dbname=$dbname user=$user password=$password");
if (!$conn) {
die("Disconnect " . pg_last_error());
}
$query = "SELECT * FROM items";
$result = pg_query($conn, $query);

if (pg_num_rows($result) > 0) {
    
	
		echo "<div>";
		echo "<h1>Sneaker Shop</h1>";
		echo "</div>";
	
	  $query = "SELECT * FROM items ORDER BY id";
	  $result = pg_query($conn, $query);
	  while ($row = pg_fetch_assoc($result)) {
		echo "<div>";
		echo "<h2>" . $row['name'] . "</h2>";
		echo "<img src='".$row['image_url']."' alt='Product Image'>";
		echo "<p>Count: " . $row['quantity'] . "</p>";
		echo "<p>Price: $" . $row['price'] . "</p>";
		echo "<form method='post' action=''>";
		echo "<input type='hidden' name='item_id' value='" . $row['id'] . "' />";
		echo "<input type='submit' name='add_to_cart' value='Add to cart' />";
		echo "</form>";
		echo "</div>";
	  }
	  if (isset($_POST['add_to_cart'])) {
		$item_id = $_POST['item_id'];
		$query = "SELECT * FROM items WHERE id = $item_id";
		$result = pg_query($conn, $query);
		$item = pg_fetch_assoc($result);
		if ($item['quantity'] > 0) {
		  $new_quantity = $item['quantity'] - 1;
		  $query = "UPDATE items SET quantity = $new_quantity WHERE id = $item_id";
		  pg_query($conn, $query);
		  echo "<p>Item added to cart</p>";
		} else {
		  echo "<p>Item out of stock</p>";
		}
	  }
} else {
    echo "goods are over";
}

pg_close($conn);
?>

</body>
</html>
