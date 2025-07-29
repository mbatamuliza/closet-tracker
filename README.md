# Closet Tracker   
General Assembly Django CRUD Project 4  

**Student:** Mary Tracy Batamuliza Nalwadda  
**Project Title:** Closet Tracker  

---

## Project Summary  
Closet Tracker is a full-stack Django web application that helps users manage and organize their personal wardrobe digitally. Users can log in, add clothing items, view their entire closet, update item details, and delete items they no longer own.  

The goal is to provide a simple but powerful digital closet solution that keeps track of fashion pieces by type, color, size, and more — all secured by user authentication.

---

## Key Features  
- Full CRUD functionality for clothing items  
- Each item is tied to the logged-in user  
- Users must log in to create, update, or delete items  
- Stylish and easy-to-navigate interface using Django templates and CSS Grid/Flexbox  
- PostgreSQL as the database  
- Deployed on Heroku for public access  

---

## Model: `ClothingItem`  

| Field       | Type         | Description                              |
|-------------|--------------|------------------------------------------|
| `name`      | Short text   | Name of the item (e.g., “Black Blazer”)  |
| `category`  | Short text   | Type of clothing (e.g., “Jacket”)        |
| `color`     | Short text   | Main color                               |
| `size`      | Short text   | Clothing size (optional)                 |
| `image_url` | URL          | Optional image link                      |
| `notes`     | Long text    | Optional notes or description            |
| `user`      | Foreign Key  | Connects to the user who owns the item   |

---

## Technologies Used  
- Django (Python)  
- PostgreSQL  
- Django Templating Engine  
- HTML / CSS (Flexbox / Grid)  
- Django Authentication  
- Git & GitHub  
- Deployed via Heroku  

---

## Why This App?  
This project is inspired by my love for fashion and organization. Closet Tracker allows users to stay on top of what they own, simplify outfit planning, and avoid buying duplicates — all through a sleek, custom-built web application.

---

## Stretch Goals  
- Filter closet items by category or season  
- Allow users to upload images instead of using links  
- Create outfit sets or looks using grouped items  
- Track when items were last worn  

---

Built with love and style by **Mary Tracy Nalwadda** aka **LadyBlac**
