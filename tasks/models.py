from django.db import models


# task = onekgula employee ekta task
# employee = onekgula task er jonno assign ase


class Employee(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    # tasks
    def __str__(self):
        return self.name
    

class Task(models.Model):
    # project = models.ForeignKey(
    #     "Project",
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True
    # )
    # notun_string = models.CharField(max_length=100, default="")

    STATUS_CHOICES = {
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed')
    }

    project = models.ForeignKey(
        "Project",
        on_delete = models.CASCADE,
        default = 1
    )

    # assigned_to = models.ManyToManyField(Employee)
    assigned_to = models.ManyToManyField(Employee, related_name='tasks')

    # notun_string = models.CharField(max_length=100, default="")

    title = models.CharField(max_length = 250)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(
        max_length = 15, choices = STATUS_CHOICES, default = "PENDING")
    is_completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

# One to One
# Many to One
# Many to Many


class TaskDetail(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low')
    )

    task = models.OneToOneField(
        Task, on_delete = models.CASCADE,
        related_name ="details"
    )
    # assigned_to = models.CharField(max_length = 100)
    priority = models.CharField(
        max_length = 1, choices = PRIORITY_OPTIONS, default = LOW
    )
    notes = models.TextField(blank = True, null = True)

    def __str__(self):
        return f"Details form Task {self.task.title}"


# Task.objects.get(id = 2)
# select * from task where id = 2
# ORM


class Project(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True, null = True)
    start_date = models.DateField()

    def __str__(self):
        return self.name





