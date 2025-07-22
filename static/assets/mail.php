<?php

// Set the content-type to JSON for response
header('Content-Type: application/json');

// Define an array to store errors and success messages
$response = array();

// Check if the necessary form fields are filled
if (isset($_POST['first_name']) && !empty($_POST['first_name']) &&
    isset($_POST['last_name']) && !empty($_POST['last_name']) &&
    isset($_POST['email']) && !empty($_POST['email']) &&
    isset($_POST['birth_date']) && !empty($_POST['birth_date']) &&
    isset($_POST['country']) && !empty($_POST['country']) &&
    isset($_POST['postal_code']) && !empty($_POST['postal_code']) &&
    isset($_POST['address']) && !empty($_POST['address'])
) {

    // Get the form data
    $first_name = $_POST['first_name'];
    $last_name = $_POST['last_name'];
    $email = $_POST['email'];
    $birth_date = $_POST['birth_date'];
    $country = $_POST['country'];
    $postal_code = $_POST['postal_code'];
    $address = $_POST['address'];

    // For the sake of example, let's pretend we're sending the email here.
    // You can use mail() function or any other mailing library.
    // Below is a dummy success message.
    
    $response['status'] = 'success';
    $response['message'] = 'Your message has been sent successfully.';

    // Here, you can process the data or send an email, save it to a database, etc.
    // For example:
    // mail($email, "Form Submission", "Thank you for contacting us!");

} else {
    // If any required field is missing, return an error message
    $response['status'] = 'error';
    $response['message'] = 'There was a problem with your submission, please try again.';
}

// Return the response in JSON format
echo json_encode($response);

?>
