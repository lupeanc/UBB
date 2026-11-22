<?php

// FOR EACH - SETTING ACTUAL PARAMETERS -------------------------------------- gym2
$classes = array();
foreach($classes as &$class){
    $stmt = $this->pdo->prepare("SELECT * FROM classes c INNER JOIN bookings b ON b.classId=c.id WHERE b.cancelled=0 AND c.id=:classId");
    $stmt->bindParam(":classId", $class['id']);
    $stmt->execute();

    $spotsTaken = $stmt->fetchAll();
    $spots = count($spotsTaken);
    // SET ACTUAL PARAMETER, NOT JUST THE COPY OF IT
    $class['maxCapacity'] -= $spots;
}

//SUBSTRING --------------------------------------
$name = "aaa";
$containsA = str_contains($name, "a");

// ELEMS IN ARRAY --------------------------------------
$elemCount = count($classes);

// NEW OBJ FROM STMT->FETCH -------------------------------------- gymclass
$row = "stmt->fetchAll()";
$model = new ModelClass($row["id"], $row["name"]);

// BINDVALUE - FOR STRING CONCATENATION -------------------------------------- personcourses
$stmt = $this->pdo->prepare("SELECT * FROM users WHERE name=:name");
$stmt->bindValue(":name", "%" . $name . "%");

// SOME STRING BS --------------------------------------
$result = array();
$grades = $result; // e.g. "Alex:9,Elena:10"
$student = "aaa";
$grade=0;

$studentFound = false;
// --------------------------------------
$pairs = explode(',', $grades);
// --------------------------------------
for ($i = 0; $i < count($pairs); $i++) {

    list($name, $currentGrade) = explode(':', $pairs[$i]);

    if ($name == $student) {
        $pairs[$i] = $student . ":" . $grade; // update grade
        $studentFound = true;
        break;
    }
}
// --------------------------------------

if (!$studentFound) {
    $pairs[] = $student . ":" . $grade; // add new grade
}

$newGrades = implode(',', $pairs);

// USEFUL --------------------------------------
