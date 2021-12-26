# Book_Inventory
It is a web application for book inventory management. Imagine you are managing a bookstore and need to keep track of inventory (i.e.,number of copies) you have on every book. On the backend, you need to keep track of books (along with their respective ID from Google Book API) and their inventory count. When a book stock goes to zero, it is considered out of stock.

## Features of portal
1. Create a login system
2. List of all stores for the user
3. List out all the books in inventory inside the store.

### Changes in the inventory
1. Add a new book
2. Update inventory for an existing book.
3. Remove from the inventory.

## Process of navigation
### 1. The first step is the login system where the user can login or create a new account to access his stores.<br />

![Create New Account](/WebsiteImages/createaccount.png)
<br />
![Login](/WebsiteImages/login.png)

<br />
<br />

### 2. After successful login, the user will be able to see all his available stores.<br />

![View All Stores](/WebsiteImages/stores_overview.png)
<br />
<br />

### 3. The user can add new stores by clicking on ```Add Store```
<br />

![Add Store](/WebsiteImages/new_store.png)
<br />
<br />

![View New Store](/WebsiteImages/viewnewstore.png)
<br />
<br />
### 4. The user can also edit store name by clicking on :pencil2: ```Edit```   <br />

![Edit Store](/WebsiteImages/edit_store_name.png)
<br />

### 5. The user should click in the store name. On clicking the respective store name, the user will directed to the books store in that store.<br />
<br />

![View Books](/WebsiteImages/books_in_store.png)
<br />
<br />

### 6. The user can add new books by clicking on ```Add Book```<br />
<br />

![Add Books](/WebsiteImages/add_new_book.png)
<br />
<br />

### 7. The user can edit only the quantity of books available in his stock. The number of books are given by using the ```google book api``` with the attribute `totalItems`
       > If the quantity is 0 then it displays Out of Stock
       > If name is to be changed, then the user should delete the book and create a new book
       
<br />

![Edit Book](/WebsiteImages/edit_new_book.png)
<br />

![Display All](/WebsiteImages/display_final.png)
<br />
<br />

### 8. The user can delete store or book by clicking on :wastebasket: `Delete` present beside the store and book.
<br />
<br />

![Delete Book](/WebsiteImages/delete_book.png)
<br />

![Display After Deletion](/WebsiteImages/new_book_deleted.png)
<br />
<br />

### 9. The user can then logout from the database by clicking on the logout present in the corner. This will logout the user and take the user back to the login page.<br />
<br />

![Logout](/WebsiteImages/logout.png)
<br />
![Redirect to login](/WebsiteImages/login.png)
