# Django Blog Application

A feature-rich blog application built with Django that allows users to create, edit, and delete posts. The application includes a homepage that lists all published blog posts and dedicated detail pages for each post.

## Features

- User authentication for blog authors
- Create, edit, and publish blog posts
- Admin interface for content management
- Responsive design using Bootstrap
- Post status system (Draft/Published)
- Slug-based URLs for SEO-friendly post links
- Featured post sidebar

## Enhancement: Comment System

- Comment model with moderation capabilities
- Admin interface for approving comments
- Ability to attach comments to specific posts

## Installation

1. **Clone the repository**

```
git clone cd django-blog
```

2. **Set up a virtual environment**

**For Windows:**

```
git clone cd django-blog
```

**For Mac/Linux:**

```
python3 -m venv venv source venv/bin/activate
```

3. **Install dependencies**

```
pip install Django
```

4. **Run migrations**

```
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser**

```
python manage.py createsuperuser
```

6. **Run the development server**

```
python manage.py runserver
```

7. **Access the application**

- Blog: http://127.0.0.1:8000/
- Admin interface: http://127.0.0.1:8000/admin/

## Usage

### Admin Interface

1. Navigate to http://127.0.0.1:8000/admin/
2. Log in with your superuser credentials
3. Manage posts, comments, and users

### Creating a Post

1. Log in to the admin interface
2. Click on "Posts" > "Add Post"
3. Fill in the title, slug, content, and set status
4. Click "Save"

### Managing Comments

1. Log in to the admin interface
2. Click on "Comments" > "Add Comment" or view existing comments
3. You can approve/reject comments using the admin actions

## Models

### Post Model

- `title`: CharField - Title of the post
- `slug`: SlugField - URL-friendly version of the title
- `author`: ForeignKey - Reference to User model
- `content`: TextField - Main content of the post
- `created_on`: DateTimeField - Auto-generated timestamp
- `updated_on`: DateTimeField - Auto-updated timestamp
- `status`: IntegerField - Publication status (Draft/Published)

### Comment Model (Week 5)

- `post`: ForeignKey - Reference to Post model
- `name`: CharField - Commenter's name
- `email`: EmailField - Commenter's email
- `body`: TextField - Comment content
- `created_on`: DateTimeField - Auto-generated timestamp
- `active`: BooleanField - Comment approval status

## Views

- `PostList`: ListView that displays published posts on the homepage
- `PostDetail`: DetailView that displays a specific post

## Test Screenshots

![alt text](/TestImages/Posts.png)
![alt text](/TestImages//Comments.png)
![alt text](/TestImages/View.png)
