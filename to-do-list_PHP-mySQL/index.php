<?php include("database.php"); ?>

<?php include('static/header.php'); ?>

<main class="container-fluid mb-3 taskSize">
  <?php
    $query = "SELECT * FROM tasks;";
    $result_tasks = mysqli_query($conn, $query);    

    while($row = mysqli_fetch_assoc($result_tasks)) { ?>

    <div class="card mb-3">
      <div class="card-body">
      <div class="row align-items-start">
        <div class="col-9 mb-2">
          <input class="form-check-input check" type="checkbox" value="" onclick="toogleFunction()">
          <label class="form-check-label" for="flexCheckDefault"><?php echo $row['title']; ?></label>
        </div>
        <div class="col-3 mb-2 text-center"><?php echo $row['date']; ?></div>
      </div>
        <div class="row align-items-end">
          <div class="col-9"><?php echo $row['description']; ?></div>
          <div class="col-3 text-center">
            <a href="edit_task.php?task_id=<?php echo $row['task_id']?>" class="btn btn-primary">Edit</a>
          </div>
        </div>
      </div>
    </div>

  <?php } ?>

  <div class="text-center ">
    <a href="add_task.php" class="btn btn-primary mb-2 btn-lg">Add new</a>
  </div>
</main>

<?php include('static/footer.php'); ?>
