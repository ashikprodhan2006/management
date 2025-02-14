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
        Task, on_delete = models.DO_NOTHING,
        related_name ="details"
    )
    priority = models.CharField(
        max_length = 1, choices = PRIORITY_OPTIONS, default = LOW
    )
    notes = models.TextField(blank = True, null = True)

    def __str__(self):
        return f"Details form Task {self.task.title}"


class Project(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True, null = True)
    start_date = models.DateField()

    def __str__(self):
        return self.name

# /////////////////////////////////////////////

class Event(models.Model):
    name = models.CharField(max_length=200, verbose_name="Event Name")
    date = models.DateField(verbose_name="Event Date")
    description = models.TextField(verbose_name="Event Description", blank=True)

    def __str__(self):
        return self.name


