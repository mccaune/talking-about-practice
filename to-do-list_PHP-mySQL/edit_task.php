<?php

include("database.php");
$title = '';
$description = '';


//getting specific task data from database
if  (isset($_GET['task_id'])) {
  $task_id = $_GET['task_id'];
  $query = "SELECT * FROM tasks WHERE task_id = $task_id;";
  $result = mysqli_query($conn, $query);
  $row = mysqli_fetch_array($result);
  $title = $row['title'];
  $description = $row['description'];
}

//for editing current task
if (isset($_POST['edit_task'])) {
  $task_id = $_GET['task_id'];
  $title = mysqli_real_escape_string($conn, $_POST['title']);
  $description = mysqli_real_escape_string($conn, $_POST['description']);
  $query = "UPDATE tasks SET title = '$title', description = '$description' WHERE task_id = $task_id;";
  mysqli_query($conn, $query);
  header('Location: index.php');
}

//for deleting current task
if(isset($_POST['delete_task'])) {
  $task_id = $_GET['task_id'];
  $query = "DELETE FROM tasks WHERE task_id = $task_id;";
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
          <form method="POST" action="edit_task.php?task_id=<?php echo $_GET['task_id'];?>" enctype="multipart/form-data">
              <div class="mb-2">
                  <h5>Title</h5>
                  <div class="form-group mb-2">
                    <input type="text" name="title" class="form-control" value="<?php echo $title;?>" placeholder="Task Title" autofocus>
                  </div>
                  <h5>Description</h5>
                  <div class="form-group mb-2">
                      <textarea name="description" rows="3" class="form-control" placeholder="Task Description"><?php echo $description;?></textarea>
                  </div>
              </div>
              <div class="text-center">
                  <input type="submit" class="btn btn-danger btn-md" name="delete_task" value="Delete">
                  <input type="submit" class="btn btn-success btn-md" name="edit_task" value="Save">
                  <a href="index.php" class="btn btn-primary btn-md">Go Back</a>
              </div>
          </form>
      </div>
		</div>
	</div>
</main>

<?php include('static/footer.php'); ?>
