
CREATE TABLE Users (
  ID char(9) NOT NULL,
  FirstName varchar(15) NOT NULL,
  LastName varchar(15) NOT NULL,
  email varchar(50) DEFAULT NULL,
  Street varchar(30) DEFAULT NULL,
  City varchar(15) DEFAULT NULL,
  State varchar(15) DEFAULT NULL,
  Country varchar(15) DEFAULT NULL,
  PRIMARY KEY (ID)
);

CREATE TABLE PhoneNumbers (
  ID char(9) NOT NULL,
  PhoneNumber decimal(10,0) NOT NULL,
  PRIMARY KEY (ID,PhoneNumber),
  CONSTRAINT phonenumbers_ibfk_1 FOREIGN KEY (ID) REFERENCES `Users` (ID)
);


CREATE TABLE Universities (
  `Name` varchar(30) NOT NULL,
  RFName varchar(15) DEFAULT NULL,
  RLName varchar(15) DEFAULT NULL,
  Street varchar(30) DEFAULT NULL,
  City varchar(15) DEFAULT NULL,
  State varchar(15) DEFAULT NULL,
  Country varchar(15) DEFAULT NULL,
  PRIMARY KEY (`Name`)
);

CREATE TABLE Students (
  ID char(9) NOT NULL,
  Major varchar(30) DEFAULT NULL,
  `Year` decimal(1,0) DEFAULT NULL,
  University varchar(30) DEFAULT NULL,
  DOB varchar(12) DEFAULT NULL,
  `Status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (ID),
  KEY University (University),
  CONSTRAINT students_ibfk_1 FOREIGN KEY (ID) REFERENCES `Users` (ID),
  CONSTRAINT students_ibfk_2 FOREIGN KEY (University) REFERENCES Universities (`Name`)
);

CREATE TABLE BookDetails (
  Title varchar(300) DEFAULT NULL,
  ISBN decimal(15,0) NOT NULL,
  ISBN13 decimal(15,0) DEFAULT NULL,
  DPublished varchar(12) DEFAULT NULL,
  Quantity decimal(4,0) DEFAULT NULL,
  Publisher varchar(50) DEFAULT NULL,
  Edition decimal(4,0) DEFAULT NULL,
  `Language` varchar(15) DEFAULT NULL,
  Category varchar(300) DEFAULT NULL,
  Author varchar(100) DEFAULT NULL,
  PRIMARY KEY (ISBN)
);

CREATE TABLE Departments (
  University varchar(30) NOT NULL,
  `Name` varchar(180) NOT NULL,
  PRIMARY KEY (University,`Name`),
  CONSTRAINT departments_ibfk_1 FOREIGN KEY (University) REFERENCES Universities (`Name`)
);

CREATE TABLE Instructors (
  ID char(9) NOT NULL,
  University varchar(30) DEFAULT NULL,
  FirstName varchar(15) DEFAULT NULL,
  LastName varchar(15) DEFAULT NULL,
  Department varchar(70) DEFAULT NULL,
  Email varchar(30) DEFAULT NULL,
  PRIMARY KEY (ID),
  KEY University (University),
  CONSTRAINT instructors_ibfk_1 FOREIGN KEY (University) REFERENCES Universities (`Name`)
);

CREATE TABLE Courses (
  ID varchar(70) NOT NULL,
  University varchar(30) NOT NULL,
  Department varchar(70) DEFAULT NULL,
  PRIMARY KEY (ID,University),
  KEY University (University),
  CONSTRAINT courses_ibfk_1 FOREIGN KEY (University) REFERENCES Universities (`Name`)
);

CREATE TABLE CourseReq (
  ISBN decimal(15,0) NOT NULL,
  CourseID varchar(70) NOT NULL,
  University varchar(30) NOT NULL,
  PRIMARY KEY (ISBN,CourseID,University),
  KEY CourseID (CourseID),
  KEY University (University),
  CONSTRAINT coursereq_ibfk_1 FOREIGN KEY (ISBN) REFERENCES BookDetails (ISBN),
  CONSTRAINT coursereq_ibfk_2 FOREIGN KEY (CourseID) REFERENCES Courses (ID),
  CONSTRAINT coursereq_ibfk_3 FOREIGN KEY (University) REFERENCES Universities (`Name`)
);

CREATE TABLE TeachingCourse (
  InstructorID char(9) NOT NULL,
  CourseID varchar(70) NOT NULL,
  Semester varchar(10) DEFAULT NULL,
  `Year` decimal(4,0) DEFAULT NULL,
  PRIMARY KEY (InstructorID,CourseID),
  KEY CourseID (CourseID),
  CONSTRAINT teachingcourse_ibfk_1 FOREIGN KEY (InstructorID) REFERENCES Instructors (ID),
  CONSTRAINT teachingcourse_ibfk_2 FOREIGN KEY (CourseID) REFERENCES Courses (ID)
);



CREATE TABLE BookInven (
  BookID char(9) NOT NULL,
  ISBN decimal(15,0) DEFAULT NULL,
  Cost decimal(5,2) DEFAULT NULL,
  BCondition varchar(10) DEFAULT NULL,
  CopyType varchar(10) DEFAULT NULL,
  Weight double(100,15) DEFAULT NULL,
  PurchaseType varchar(15) DEFAULT NULL,
  PRIMARY KEY (BookID),
  KEY ISBN (ISBN),
  CONSTRAINT bookinven_ibfk_3 FOREIGN KEY (ISBN) REFERENCES BookDetails (ISBN)
);

CREATE TABLE BookHis (
  StudentID char(9) NOT NULL,
  ISBN decimal(15,0) DEFAULT NULL,
  PRIMARY KEY (StudentID),
  KEY ISBN (ISBN),
  CONSTRAINT bookhis_ibfk_1 FOREIGN KEY (StudentID) REFERENCES Students (ID),
  CONSTRAINT bookhis_ibfk_2 FOREIGN KEY (ISBN) REFERENCES BookDetails (ISBN)
);

CREATE TABLE Keywords (
  ISBN decimal(15,0) NOT NULL,
  Keyword varchar(300) NOT NULL,
  PRIMARY KEY (ISBN,Keyword),
  CONSTRAINT keywords_ibfk_1 FOREIGN KEY (ISBN) REFERENCES BookDetails (ISBN)
);

CREATE TABLE Subcategories (
  ISBN decimal(15,0) NOT NULL,
  Subcategory varchar(300) NOT NULL,
  PRIMARY KEY (ISBN,Subcategory),
  CONSTRAINT subcategories_ibfk_1 FOREIGN KEY (ISBN) REFERENCES BookDetails (ISBN)
);

CREATE TABLE BooksRented (
  StudentID char(9) NOT NULL,
  BookID char(9) NOT NULL,
  DateDue varchar(12) DEFAULT NULL,
  DateRented varchar(12) DEFAULT NULL,
  Cost decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (StudentID,BookID),
  KEY BookID (BookID),
  CONSTRAINT booksrented_ibfk_1 FOREIGN KEY (StudentID) REFERENCES Students (ID),
  CONSTRAINT booksrented_ibfk_2 FOREIGN KEY (BookID) REFERENCES BookInven (BookID)
);

CREATE TABLE BooksBought (
  StudentID char(9) NOT NULL,
  BookID char(9) NOT NULL,
  DateBought varchar(12) DEFAULT NULL,
  Cost decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (StudentID,BookID),
  KEY BookID (BookID),
  CONSTRAINT booksbought_ibfk_1 FOREIGN KEY (StudentID) REFERENCES Students (ID),
  CONSTRAINT booksbought_ibfk_2 FOREIGN KEY (BookID) REFERENCES BookInven (BookID)
);

CREATE TABLE CartDateCreated(
  StudentID char(9) NOT NULL,
  DCreated varchar(12) DEFAULT NULL,
  PRIMARY KEY (StudentID)
);
CREATE TABLE CartDateUpdated(
  StudentID char(9) NOT NULL,
  DUpdated varchar(12) DEFAULT NULL,
  PRIMARY KEY (StudentID)
);

CREATE TABLE Cart (
  StudentID char(9) NOT NULL,
  ISBN decimal(15,0) NOT NULL,
  RentBuy varchar(5) DEFAULT NULL,
  Quantity decimal(4, 0) DEFAULT NULL,
  Wishlist char(1) DEFAULT NULL,
  PRIMARY KEY (StudentID, ISBN),
  KEY ISBN (ISBN),
  CONSTRAINT cart_ibfk_1 FOREIGN KEY (StudentID) REFERENCES Students (ID),
  CONSTRAINT cart_ibfk_2 FOREIGN KEY (ISBN) REFERENCES BookDetails (ISBN)
);


CREATE TABLE Employees (
  EmployeeID char(9) NOT NULL,
  Gender varchar(8) DEFAULT NULL,
  Salary decimal(8,2) DEFAULT NULL,
  SSN char(11) DEFAULT NULL,
  PRIMARY KEY (EmployeeID),
  CONSTRAINT employees_ibfk_1 FOREIGN KEY (EmployeeID) REFERENCES `Users` (ID)
);



CREATE TABLE SuperAdmin (
  EmployeeID char(9) NOT NULL,
  PRIMARY KEY (EmployeeID),
  CONSTRAINT superadmin_ibfk_1 FOREIGN KEY (EmployeeID) REFERENCES Employees (EmployeeID)
);

CREATE TABLE Admin (
  EmployeeID char(9) NOT NULL,
  AddedBy char(9) DEFAULT NULL,
  PRIMARY KEY (EmployeeID),
  KEY AddedBy (AddedBy),
  CONSTRAINT admin_ibfk_1 FOREIGN KEY (EmployeeID) REFERENCES Employees (EmployeeID),
  CONSTRAINT admin_ibfk_2 FOREIGN KEY (AddedBy) REFERENCES SuperAdmin (EmployeeID)
);


CREATE TABLE CustomerSupport (
  EmployeeID char(9) NOT NULL,
  AddedBy char(9) DEFAULT NULL,
  PRIMARY KEY (EmployeeID),
  KEY AddedBy (AddedBy),
  CONSTRAINT customersupport_ibfk_1 FOREIGN KEY (EmployeeID) REFERENCES Employees (EmployeeID),
  CONSTRAINT customersupport_ibfk_2 FOREIGN KEY (AddedBy) REFERENCES SuperAdmin (EmployeeID)
);



CREATE TABLE TroubleTickets (
  TicketNumber varchar(5) NOT NULL,
  TicketCategory varchar(15) DEFAULT NULL,
  Title varchar(60) DEFAULT NULL,
  Description varchar(300) DEFAULT NULL,
  Solution varchar(300) DEFAULT NULL,
  HandledBy char(9) DEFAULT NULL,
  AssignedTo char(9) DEFAULT NULL,
  PRIMARY KEY (TicketNumber)
);


CREATE TABLE TicketStatusHistory (
  TicketNumber varchar(5) NOT NULL,
  TicketStatus varchar(15) NOT NULL,
  ChangeDate varchar(12) NOT NULL,
  PRIMARY KEY (TicketNumber,TicketStatus,ChangeDate),
  CONSTRAINT ticketstatushistory_ibfk_2 FOREIGN KEY (TicketNumber) REFERENCES TroubleTickets (TicketNumber)
);


CREATE TABLE Orders (
  StudentID char(9) NOT NULL,
  BookISBN decimal(15,0) NOT NULL,
  RentBuy varchar(15) NOT NULL,
  Quantity decimal(3,0) DEFAULT NULL,
  DateCreated varchar(12) NOT NULL,
  DateFulfilled varchar(12) DEFAULT NULL,
  SType varchar(10) DEFAULT NULL,
  CCNumber varchar(20) DEFAULT NULL,
  CCExpiration varchar(12) DEFAULT NULL,
  CCName varchar(15) DEFAULT NULL,
  CCType varchar(15) DEFAULT NULL,
  OStatus varchar(10) DEFAULT NULL,
  PRIMARY KEY (StudentID, BookISBN, RentBuy, DateCreated),
  KEY StudentID (StudentID),
  CONSTRAINT orders_ibfk_1 FOREIGN KEY (StudentID) REFERENCES Students (ID)
);


CREATE TABLE BRecommended (
  StudentID char(9) NOT NULL,
  BookISBN decimal(15,0) DEFAULT NULL,
  PRIMARY KEY (StudentID),
  KEY BookISBN (BookISBN),
  CONSTRAINT brecommended_ibfk_1 FOREIGN KEY (StudentID) REFERENCES Students (ID),
  CONSTRAINT brecommended_ibfk_2 FOREIGN KEY (BookISBN) REFERENCES BookDetails (ISBN)
);

CREATE TABLE BReviewed (
  StudentID char(9) DEFAULT NULL,
  RTitle varchar(50) DEFAULT NULL,
  Rating decimal(1,0) DEFAULT NULL,
  BookISBN decimal(15,0) DEFAULT NULL,
  RDescription varchar(500) DEFAULT NULL,
  KEY StudentID (StudentID),
  KEY BookISBN (BookISBN),
  CONSTRAINT breviewed_ibfk_1 FOREIGN KEY (StudentID) REFERENCES Students (ID),
  CONSTRAINT breviewed_ibfk_2 FOREIGN KEY (BookISBN) REFERENCES BookDetails (ISBN)
);




CREATE TABLE TakingCourse (
  StudentID char(9) NOT NULL,
  CourseID varchar(70) NOT NULL,
  Semester varchar(10) DEFAULT NULL,
  PRIMARY KEY (StudentID,CourseID),
  KEY CourseID (CourseID),
  CONSTRAINT takingcourse_ibfk_1 FOREIGN KEY (StudentID) REFERENCES Students (ID),
  CONSTRAINT takingcourse_ibfk_2 FOREIGN KEY (CourseID) REFERENCES Courses (ID)
);
