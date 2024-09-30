from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Contact
class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

# Posts
class Post(models.Model):
    STATUS = (
        ('0', 'Draft'),
        ('1', 'Publish'),
    )
    SECTION = (
        ('Recent', 'Recent'),
        ('Popular', 'Popular'),
        ('Trending', 'Trending'),
        ('Latest Posts', 'Latest Posts'),
        # ('Latest Posts', 'Latest Posts'),
    )
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    header_image = models.ImageField( upload_to='image/', null=True, blank=True)
    writer = models.CharField(max_length=200, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    first_content = models.TextField(max_length=200, null=True)
    content = models.TextField()
    # category = models.ForeignKey(on_delete=models.SET_NULL, related_name='category', blank=True, null=True)
    image = models.ImageField( upload_to='image/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(choices=STATUS, max_length=100, default=0, null=True)
    section = models.CharField(choices=SECTION, max_length=200, default='Recent', null=True)
    add_more = models.CharField(choices=SECTION, max_length=200, default='Recent', null=True)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

# Review Posts
class ReviewPost(models.Model):
    STATUS = (
        ('1', 'Draft'),
        ('2', 'Publish'),
    )
    writer = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    career = models.CharField(max_length=100, unique=True)
    hospital = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(choices=STATUS, max_length=100, default=1, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.writer


# Featured Posts
class FeaturedPost(models.Model):
    STATUS = (
        ('0', 'Draft'),
        ('1', 'Publish'),
    )
    SECTION = (
        ('Popular', 'Popular'),
        ('Recent', 'Recent'),
        ('Trending', 'Trending'),
        ('Latest Posts', 'Latest Posts'),
    )
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    header_image = models.ImageField(upload_to='image/', null=True, blank=True)
    writer = models.CharField(max_length=200, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    first_content = models.TextField(max_length=200, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(choices=STATUS, max_length=100, default=0, null=True)
    section = models.CharField(choices=SECTION, max_length=200, default='Recent')
    add_more = models.CharField(choices=SECTION, max_length=200, default='Recent', null=True)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

# User Profiles
class UserProfile(models.Model):
    FEMALE = 'FEMALE'
    MALE = 'MALE'

    CHOICES = [
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # id_user = models.ImageField()
    name = models.CharField(max_length=300)
    email = models.EmailField()
    username = models.CharField(max_length=300)
    profession = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='image/', default='blank-profile-picture.png', blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=CHOICES, default=FEMALE)
    date_of_birth = models.DateField(verbose_name=('date_of_birth'), null=True)
    created_at = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=300, null=True, blank=True)
    zip_code = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    website_url = models.CharField(max_length=300, null=True, default='https://www.yourwebsitelink.com')
    facebook_url = models.CharField(max_length=300, null=True, default='https://www.yourfacebooklink.com')
    twitter_url = models.CharField(max_length=300, null=True, default='https://www.yourtwitterlink.com')
    instagram_url = models.CharField(max_length=300, null=True, default='https://www.yourinstagramlink.com')
    youtube_url = models.CharField(max_length=300, null=True, default='https://www.youryoutubelink.com')
    linkedin_url = models.CharField(max_length=300, null=True, default='https://www.yourlinkedinlink.com')

    def __str__(self):
        return self.username


# Daily Review
class DailyReview(models.Model):
    STATUS = (
        ('1', 'Draft'),
        ('2', 'Publish'),
    )
    image = models.ImageField(upload_to='image/', default='blank-profile-picture.png', blank=True, null=True)
    title = models.CharField(max_length=300, null=True)
    content = models.TextField(max_length=300)
    doctor = models.CharField(max_length=200, null=True)
    status = models.CharField(choices=STATUS, max_length=100, default=1, null=True)

    # class Meta:
    #     ordering = ['-created_on']

    def __str__(self):
        return self.doctor