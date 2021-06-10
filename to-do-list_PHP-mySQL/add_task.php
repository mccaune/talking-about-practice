<?php 

include('database.php');

if (isset($_POST['save_task'])) {
    $title = mysqli_real_escape_string($conn, $_POST['title']);
    $description = mysqli_real_escape_string($conn, $_POST['description']);
    $query = "INSERT INTO tasks(title, description) VALUES ('$title', '$description');";
    $result = mysqli_query($conn, $query);
    header('Location: index.php');
}

?>

<?php include('static/header.php'); ?>

<main>
    <div class="center">
		<div class="card" style="width: 32rem;">
            <div class="card-body" >
                <h4 class="text-center">Add new</h4>
                <form method="POST" action="add_task.php" enctype="multipart/form-data">
                    <div class="mb-2">
                        <h5>Title</h5>
                        <div class="form-group mb-2">
                        <input type="text" name="title" class="form-control" placeholder="Task Title" autofocus>
                        </div>
                        <h5>Description</h5>
                        <div class="form-group mb-2">
                            <textarea name="description" rows="3" class="form-control" placeholder="Task Description"></textarea>
                        </div>
                    </div>
                    <div class="text-center">
                        <input type="submit" class="btn btn-success btn-md" name="save_task" value="Add">
                        <a href="index.php" class="btn btn-primary btn-md">Go Back</a>
                    </div>
                </form>
            </div>
		</div>
	</div>
</main>

<?php include('static/footer.php'); ?>
