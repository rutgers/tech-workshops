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

## Module 2 - It'a Tag  /Tag World! 

1. As mentioned, HTML is built all around what we call "tags". Tags basically tell the broswer how to interpret certain blocks of code. By its nature, HTML is a hiearchical language where the placement of the tag helps define the webpage we are creating. There are are four main tags that we will cover: 
 ``` html
 <html> ,<h#>, <body>, <div> 
```

2. As you might notice above every "tag" comes in a pair with an opening and closing tag. Every html document is started with the <html> opening tag so that the broswer knows that everything between <html> and </html> is to be interpreted as HTML code. Without this tag, none of the other tags will get formatted properly :
instead the webpage would simply display all the tags:
```html
<head>
 <title>Heading Example <title> 
 </head> 
 .... 
 //Also remember to close every tag!
```




## Module 3 - A Basic Template

First, download the template named carousel.html that can be found in this folder. Then, try opening the file with your browser of choice. This template features a carousel that automatically switches between multiple photos in addition to a responsive navbar. Try playing around with changing the `src` attribute of the various `img` tags to see how it changes the site.


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

## Module - References

