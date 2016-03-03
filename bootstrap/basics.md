# Rutgers IEEE Student Branch - Boostrap Basics Workshop

## Workshop Leaders

Ravi Bhankharia, Niral Shah

## Module 0 - What are HTML, CSS, Javascript and Bootstrap?

* HTML stands for HyperText Markup Language - it's the syntax that defines the layout of all webpages. It includes a webpage's text and images.

* CSS stands for Cascading Style Sheets - it's what defines the color and size of information on the webpage.

* Javascript is a programming language used in webpages that is run in your browser.

Most popular sites use all three of these languages to create responsive webpages.

* Bootstrap is a CSS Framework used to create beautiful responsive pages quickly. It's easy to use, compatible with all modern browsers, and it's mobile first.

Building a bootstrap website normally starts with a template and modifying the HTML source to match what you want

## Module 1 - HTML

HTML is built around tags - all text on a page starts and ends in a tag. For example:
```html
<!DOCTYPE html> 
<html>
<body> This is a body tag </body>
</html>
```
1. The first line at the top <!DOCTYPE html>, defines the document type. Letting the broswer know which flavor of html you are using (by default it's HTML 5, the latest version). Without this declaration you will get unexpected behavior from the browser. 

## Module 2 - It'a \<tag>  \</tag> World! 

1. As mentioned, HTML is built all around what we call "tags". Tags basically tell the broswer how to interpret certain blocks of code. By its nature, HTML is a hiearchical language where the placement of the tag helps define the webpage we are creating. There are the main tags that we will cover: 
 ``` html
 <html> ,<body>,<h#>, <div>,<a href="">,,<img>,<button>, <table>
```
##  HTML tag: 
2. As you might notice above every "tag" comes in a pair with an opening and closing tag. Every html document is started with the <html> opening tag so that the broswer knows that everything between <html> and </html> is to be interpreted as HTML code. Without this tag, none of the other tags will get formatted properly :
instead the webpage would simply display all the tags:
```html
<head>
 <title>Heading Example <title> 
 </head> 
 .... 
 //Also remember to close every tag!
```
##  Body tag: 
3. At the foundation of every webpage is just body text. Body Text is defined in this way: 
``` html
<!DOCTYPE html>
<html>
<body>
 Hello World! 
 </body> 
 </html> 

//Tip: See this for yourself! Open up notepad on your computer, copy and paste this and save the file as Test.html 
```

## Header tags:
4. When you create a document often times you want to have headers for various sections and define the title for the webpage. You can accomplish this with the title and header tags. 
```html 

<!DOCTYPE html>
<html>
//Title is what appears in title bar of your web broswer  
//The <head> tag will also be a place to define the webpage's style (more on this later)

<head>
<title> Welcome to IEEE's Website! </title> 
// In HTML there are 6 primary headers, to really understand this copy into notepad and save as header.html

</head>
<body>
<h1> This is heading 1 </h1>
<h2>This is heading 2</h2>
<h3>This is heading 3</h3>
<h4>This is heading 4</h4>
<h5>This is heading 5</h5>
<h6>This is heading 6</h6> 
</body>

</html>
```
## The Div Tag:
5. The \<div> tag defines a division or section in an html document. This may sound boring but the div tag is the workhorse of an hmtl webpage. They are extremely useful because div tags are often used to arrange elements together with CSS. Let's take a look at an example: 
``` html
<!DOCTYPE html>
<html>
<head>
<title>HTML div Tag</title>
</head>
<body>
<div id="contentinfo" style="color:#0000FF">
<h3>This is your heading</h3>
   // often times you will want to give a div an id attribute, so you can apply specific styles to it in the stylesheet
<p>Welcome to our website. We provide tutorials on various subjects.</p>
</div>
</body>
</html>
```

## Hyperlink's 
6.  An important aspect of every webpage is having clickable links otherwise known as hyperlinks. Hyperlinks are defined using the /<html><a>  or attribute tag. Let's take a look. I strongly encourage you to copy and paste this to your test doc.
``` 
<!DOCTYPE html>
<html>
<head>
<title>My First Hyperlink </title>
</head>
<h3> Hyperlink Tutorial </h3> 
<body>
<a href = https://www.youtube.com/watch?v=dQw4w9WgXcQ> A great HTML Tutorial </a> 
</body>
</html>
 ``` 
## Images 
 7. Often times you want to insert an image into a webpage. You should use the img tag. 
 ``` html
 <!DOCTYPE html> 
 <html> 
 <head>
 <title> Images </title> 
 </head> 
 <div> 
 <img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/2000px-Apple_logo_black.svg.png" 
 alt ="Apple logo" height = "48" width = "48" > 
 
 //So first thing with images is you have to define the src or file location. This could either be a url from a web or could be a local image on your computer. If you have a local image you want to make sure that image is stored in the same file location as your html file.

 </div>
```
There are many attributes that you can use to style an image. Check out this site for reference:
http://www.w3schools.com/tags/tag_img.asp 

## Buttons
8.The button tag defines a clickable button.Inside a button element you can put content like text or images. You can also define various different events that occur when the button is clicked. In this case we will open up a pop up dialog window or an alert.

``` html
<!DOCTYPE html>
<html>
<body>

<button type="button" onclick="alert('Hello world!')">Click Me!</button>
 
</body>
</html>

```

## Tables
9. Finally one of the most important html elements is the table element. Let's take a look at an example: 
``` html  
<!DOCTYPE html>
<html>
<body>

<table border="1" style="width:100%">
  <tr>
    <td>Rutgers</td>
    <td>Princeton</td>		
    <td>Harvard</td>
  </tr>
  <tr>
    <td>HackRU</td>
    <td>HackPton</td>		
    <td>HackHarvard</td>
  </tr>
  <tr>
    <td>1</td>
    <td>2</td>		
    <td>3</td>
  </tr>
</table>

</body>
</html>
``` 
The Example Decomposed: 
 - \<table> tag defines the beginning of the table, as with any html tag the style can be defined there. You must define a border otherwise by default the table will not have a border. 
 - \<tr> defines a table row
 - \<td> defines table data
 - \<th> a table row can also be divided into table headings 
  

##  CSS - Quick Summary: 


## Module 3 - A Basic Template and Testing Your Files

First, download either the template named carousel.html or template2.html that can be found in this folder. Then, try opening the file with your browser of choice. Whenever you make a change, be sure to save your html file and refresh in your browser! The first template features a carousel that automatically switches between multiple photos in addition to a responsive navbar. This is better suited for a club or organization website. Try playing around with changing the `src` attribute of the various `img` tags to see how it changes the site. The second template is a basic website featuring a jumbotron that may be better suited for a person website. 


## Module 4 - The Grid System

In order to actually add a new section, we're going to have to either create a new page or add a `<div>` tag at the bottom of the page above the footer section. Let's try adding a new div tag with the class attribute set to `container-fluid` along with another 2 more nested div tags with the class attribute set to `row` and `col`:

```html
<div class="container-fluid">
 <div class="row">
  <div class="col">
  </div>
 </div>
</div>
```

Each container in Bootstrap's grid system includes any number of rows, and any number of columns nested in those rows. In order to enable Bootstrap's responsive grid system, we need to specify the width of each column. All columns' widths must sum up to 12. This means that you can have 4 columns of width 3 or 2 columns of width 6 and etc. In addition to specifying the width of each column, you must specify the user's screen size. 

For example - 
* xs stands for extra small so it corresponds to a mobile phone.
* s stands for small so it corresponds to a small tablet.
* m stands for medium so it corresponds to a laptop.
* l stands for large so it corresponds to a standard desktop.
* xl stands for extra large so it corresponds to a wide desktop.

So on a medium screen, the user will see one grid layout, but on a mobile phone they will see another. 

If you don't specify all the widths for each screen size, each column will appear one after the other vertically if you go below the specified screen size.

If you made two medium columns of width 6 (col-md-6), if the user is using a laptop or a desktop, they will see 2 columns next to each other. However, if you're viewing it on a tablet or phone, you will see 1 column and then will have to scroll down to see the next one. Test the grid system out on your file and try changing the size of your browser window.

```html
<div class="container-fluid">
 <div class="row">
  <div class="col-md-3 col-s-4 col-xs-6">
  1
  </div>
  <div class="col-md-3 col-s-4 col-xs-6">
  2
  </div>
  <div class="col-md-3 col-s-4 col-xs-6">
  3
  </div>
  <div class="col-md-3 col-s-4 col-xs-6">
  4
  </div>
 </div>
</div>
```

## Module 5 - Images, Buttons and Tables



### Buttons

```html
<!-- Standard button -->
<button type="button" class="btn btn-default">Default</button>

<!-- Provides extra visual weight and identifies the primary action in a set of buttons -->
<button type="button" class="btn btn-primary">Primary</button>

<!-- Indicates a successful or positive action -->
<button type="button" class="btn btn-success">Success</button>

<!-- Contextual button for informational alert messages -->
<button type="button" class="btn btn-info">Info</button>

<!-- Indicates caution should be taken with this action -->
<button type="button" class="btn btn-warning">Warning</button>

<!-- Indicates a dangerous or potentially negative action -->
<button type="button" class="btn btn-danger">Danger</button>

<!-- Deemphasize a button by making it look like a link while maintaining button behavior -->
<button type="button" class="btn btn-link">Link</button>
```
Bootstrap's tables, buttons and images are pretty much the same as their normal HTML counterparts but look much better and have several more customization options.

### Tables

First, try adding a normal table to your html page and check out how it looks.

Then, try adding a `class="table"` attribute to your table tag and see how it changes.

Test out the following attribute values and see which you like the best:

```html
class="table table-striped"
class="table table-bordered"
class="table table-hover"
class="table table-condensed"
```

In addition, try adding "active", "success", "info" and "danger" to a row's class attribute as well and see how the colors change!

### Images

You can make images responsive and fill the container by adding the attribute `class="img-responsive"` to any image.

You can also change the shape of an image in bootstrap by linking an image and setting it's class ot one of the following below. Try each one to see how they look!

```html
<img src="..." alt="..." class="img-rounded">
<img src="..." alt="..." class="img-circle">
<img src="..." alt="..." class="img-thumbnail">
```

## Module 6 - Next Steps

Now that we've taught you the basics and given you a glimpse at Bootstrap's toolbox, let's take one of our 3 templates and attempt to make your own personal website!


## Module - References
https://getbootstrap.com/css/#overview
http://www.w3schools.com/
