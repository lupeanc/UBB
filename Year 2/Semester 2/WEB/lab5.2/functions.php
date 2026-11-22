<?php
require_once("connection.php");

function getAllReservations()
{
    //gets $conn from connection - which means it is a global variable, not function specific
    global $conn;
    $result = mysqli_query($conn, "SELECT * FROM reservations");

    if (mysqli_num_rows($result) > 0) {
        // while there are rows in our sql result set ...
        while ($row = mysqli_fetch_assoc($result)) {
            echo "<tr>
                        <td>" . $row['id'] . "</td>
                        <td>" . $row['user_id'] . "</td>
                        <td>" . $row['room_id'] . "</td>
                        <td>" . $row['start'] . "</td>
                        <td>" . $row['end'] . "</td>
                    </tr>";
        }

    } else echo "<h3>No reservations found!</h3>";

    // REFERS TO THE NAMES!! OF THE FIELDS
    // if the fields are set (they exist and are not null) and not empty
    if (isset($_POST['user_id']) && isset($_POST['room_id']) && isset($_POST['start']) && isset($_POST['end'])) {
        if (!empty($_POST['user_id']) && !empty($_POST['room_id']) && !empty($_POST['start']) && !empty($_POST['end'])) {
            // escape sql injections
            $user_id = mysqli_real_escape_string($conn, htmlspecialchars($_POST['user_id']));
            $room_id = mysqli_real_escape_string($conn, htmlspecialchars($_POST['room_id']));
            $start = mysqli_real_escape_string($conn, htmlspecialchars($_POST['start']));
            $end = mysqli_real_escape_string($conn, htmlspecialchars($_POST['end']));

            // do not allow user to add reservations with room ids that are occupied in the time frame they selected
            $check_availability = mysqli_query($conn, "SELECT * FROM reservations WHERE room_id = $room_id AND ('$start' BETWEEN start AND end)");

            if (mysqli_num_rows($check_availability) > 0) {
                echo "<script>alert('Already booked!');</script>";
//                exit();
            }
            else {
                $add = mysqli_query($conn, "INSERT INTO reservations (user_id, room_id, start, end) VALUES ($user_id,$room_id,'$start','$end')");
//                echo "<meta http-equiv='refresh' content='0'>";
                if ($add) {
                    echo "<script>alert('Reservation booked!');</script>";
                    // refresh
                    echo "<meta http-equiv='refresh' content='0'>";
                }
                else {
                    echo "<script>alert('Reservation could not be booked!');</script>";
                }
            }
        } else
            echo "<h4>Please fill all fields!</h4>";
    }
}
function getAllReservationsUpdate()
{
    //makes var global, not func specific
    global $conn;
    $result = mysqli_query($conn, "SELECT * FROM reservations");

    if (mysqli_num_rows($result) > 0) {
        while ($row = mysqli_fetch_assoc($result)) {
            $id = $row['id'];
            echo "<tr>
                        <td><button type='submit' name='. $id .' class='selected-id'>" . $row['id'] . "</td>
                        <td>" . $row['user_id'] . "</td>
                        <td>" . $row['room_id'] . "</td>
                        <td>" . $row['start'] . "</td>
                        <td>" . $row['end'] . "</td>
                    </tr>";
        }

    } else echo "<h3>No reservations found!</h3>";

    // REFERS TO THE NAMES!! OF THE FIELDS
    if (isset($_POST['update_user_id']) && isset($_POST['update_room_id']) && isset($_POST['update_start']) && isset($_POST['update_end'])) {
        if (!empty($_POST['update_user_id']) && !empty($_POST['update_room_id']) && !empty($_POST['update_start']) && !empty($_POST['update_end'])) {

            $id = mysqli_real_escape_string($conn, htmlspecialchars($_POST['update_id']));
            $user_id = mysqli_real_escape_string($conn, htmlspecialchars($_POST['update_user_id']));
            $room_id = mysqli_real_escape_string($conn, htmlspecialchars($_POST['update_room_id']));
            $start = mysqli_real_escape_string($conn, htmlspecialchars($_POST['update_start']));
            $end = mysqli_real_escape_string($conn, htmlspecialchars($_POST['update_end']));

            $check_availability = mysqli_query($conn, "SELECT * FROM reservations WHERE room_id = $room_id AND id != $id AND ('$start' BETWEEN start AND end)");
            if (mysqli_num_rows($check_availability) > 0) {
                echo "<h3>Already booked!</h3>";
                exit();
            }
            else {

                $update = mysqli_query($conn, "UPDATE reservations SET user_id=$user_id,room_id=$room_id,start='$start',end='$end' WHERE id=$id");
//                echo "<meta http-equiv='refresh' content='0'>";
                if($update){
                    echo "<script>alert('Reservation updated!');</script>";
                    echo "<meta http-equiv='refresh' content='0'>";
                }
                else {
                    echo "<script>alert('Unable to update Reservation!');</script>";
                }
            }
        } else
            echo "<h4>Please fill all fields!</h4>";
    }
}

function getAllReservationsDelete(){
    global $conn;
    $result = mysqli_query($conn, "SELECT * FROM reservations");

    if (mysqli_num_rows($result) > 0) {
        while ($row = mysqli_fetch_assoc($result)) {
            $id = $row['id'];
            $link="delete.php?id=$id";
            echo "<tr>
                        <td>" . $row['id'] . "</td>
                        <td>" . $row['user_id'] . "</td>
                        <td>" . $row['room_id'] . "</td>
                        <td>" . $row['start'] . "</td>
                        <td>" . $row['end'] . "</td>
                        <td>
                        <a class='delete-button' href=$link>Delete</a>
</td>
                    </tr>";
        }

    } else echo "<h3>No reservations found!</h3>";

//    get the value from the url
    if(isset($_GET['id'])){
        $id = $_GET['id'];
        $delete = mysqli_query($conn, "DELETE FROM reservations WHERE id=$id");
        if($delete){
            echo "<script>alert('Reservation deleted!');</script>";
            echo "<script>location.href='delete.php'</script>";
        }
        else {
            echo "<script>alert('Error deleting reservation!');</script>";
        }

//        echo "<meta http-equiv='refresh' content='0'>";
    }
}

function getAllReservationsFiltered()
{
    global $conn;

    $category = isset($_GET['category']) ? $_GET['category'] : '';
    $beds = isset($_GET['beds']) ? $_GET['beds'] : '';
    $price = isset($_GET['price']) ? $_GET['price'] : '';

    $page = isset($_GET['page']) ? (int)$_GET['page'] : 1;
    $limit = 4;
    // so sql skips the previous 4x entries
    $offset = ($page - 1) * $limit;

    $query = "SELECT * FROM rooms WHERE 1=1";

    if ($category != '') {
        $query .= " AND category='$category'";
    }
    if ($beds != '') {
        $query .= " AND nb_beds >= $beds";
    }
    if ($price != '') {
        $query .= " AND price <= $price";
    }

    // get the total number of rooms found
    $countQuery = str_replace("SELECT *", "SELECT COUNT(*) as total", $query);
    $countResult = mysqli_query($conn, $countQuery);
    $total = mysqli_fetch_assoc($countResult)['total'];

    // paginate(?) them - complete the query with limit and offset,
    // so we only get the current 4 entries
    $query .= " LIMIT $limit OFFSET $offset";

    $result = mysqli_query($conn, $query);

    // add all the rooms to an array
    $rooms = [];
    while ($row = mysqli_fetch_assoc($result)) {
        $rooms[] = $row;
    }

    // encode it into a json and return it
    // so it can be used with the js file
    echo json_encode([
        "rooms" => $rooms,
        "total" => $total
    ]);
}

?>