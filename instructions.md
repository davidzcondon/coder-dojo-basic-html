# Instructions

## How to start a new website

1. Create a new folder on the desktop
2. Create an index.html file in the new folder
3. Add `<html>` tags
4. Add `<head>` tag inside the html tag.
5. Add `<body>` tag inside the html tag. This goes after the head tag.
6. Add `<title>` tag inside the head tag. Give the website a title. The text between the two title tags is the website's title.
7. Add a `<h1>` heading to the website. The h1 tag needs to go inside the body tag. The text between the h1 tags is the heading.
8. Add a stylesheet to the website

## Preview website

1. After ever change you make, you should preview it in the browser (Chrome) to make sure that you have no mistakes
2. In Brackets open the index.html page and click the lightening bolt to the right of the page.
3. Another way to view the website is to go to Chrome and click refresh after saving.

## How to create a new file

1. Click `File->New`. This will bring up a blank new file.
2. Click `File->Save As`
3. Type the name of the file in the Save As box.
4. Now we need to find the folder where to save the file.
5. Click the desktop at the left of the window.
6. Click the website folder
7. Click the save button

## Make a heading move across the screen

1. Surround the heading tags with `<marquee>` tags
2. For example, `<marquee><h2>Heading</h2></marquee>`

## How to save a file

1. When there is a circle next to the file name we need to save the file
2. Click `File->Save`
3. Or you can press command and s together
4. The circle should disappear when you save the file.
5. You should save after each line

## How to copy and paste text

1. Select the text that you want to copy. It will be highlighted (normally in blue)
2. Click `Edit->Copy`
3. Move the cursor where you want the text to go.
4. Click `Edit->Paste`

## Undo - Fixing a mistake

1. If you make a mistake typing, or if you delete a line by accident, you can fix the mistake using undo.
2. Click `Edit->Undo` or press command z

## How to add a video

1. Go to www.youtube.com in the browser
2. Enter what you are looking for in the search box and press enter.
3. A list of videos will appear. Click the one you wish to add to your website.
4. Click the share button
5. Click the embed button
6. Select and copy the iframe text that appears
7. Paste it into the index.html

## How to add an image

1. Go to Google and search for the image you want. Type the text into the search bar.
2. Click the images tab to see the images.
3. Download the image to the website folder.
4. Add `<img src="image.png" height="250px" width="300px" \>` to the html file
5. You should change image.png to the name of your image
6. You can change the size of the image by changing the numbers inside the height and width parts.
7. If the image is squashed then remove either the height or the width parts.

## How to download an image

1. Right click on the image - do this by pressing control and click
2. Click `Save Image As...`
3. Enter a proper name for the image with no spaces
4. Select the correct folder to save it in

## How to add a stylesheet to a website

1. Create a new file called style.css
2. In the `index.html` file add `<link rel="stylesheet" href="style.css" />` to inside the head tag.

## How to change the background colour

1. Add a tag for html if there isn't one already. Add `html { }`
2. Inside the curly brackets add `background-color: color;`
3. Replace the cork color with either a colour name e.g. blue or a hex number from the color picker

## How to set the background image

1. Add a tag for html if there isn't one already. Add `html { }`
2. Inside the curly brackets add `background: url(image-name);`
3. Replace image-name with the name of your image. Don't forget the `.jpg` or `.png`.

## How to change the color of a Heading

1. Add a tag for h1 or whichever tag you want to change e.g. `h1 { }`
2. To change the color add `color: red;` inside the h1 tag
3. Replace red with either a color name or a hex number from the color picker

## How to change to font size of a tag

1. Add the tag if it is not there already e.g. `h1 { }` or `p { }`
2. Inside the tag add `font-size: 36px;`
3. Replace the 36 with the size in pixels that you want. Bigger numbers make the text bigger and smaller numbers make the text smaller.

## To change the type of font

1. Add the tag if it is not there already e.g. `h1 { }` or `p { }`
2. Inside the tag add `font-family: type`
3. Replace the word type with the type of font you wish to use. Examples are `sans-serif`, `serif`

## Tables

### How to create a blank table

1. Add the `<table></table>` tag to the index.html page
2. Add a border by adding `border="px"` inside the table opening tag e.g. `<table border="px"></table>`

### How to add a row for Headings

1. Add `<tr></tr>` between the table opening and closing tags to add a new row.
2. The tag for headings is `<th>` so to add a heading we add `<th>Name</th>` between the `<tr>` and `</tr>` tags
3. Change Name to be whatever your heading is
4. To add more headings just add more `<th>Name</th>` after the last `<th>`

### How to add a normal row

1. Add `<tr></tr>` to create the row. Add these after the last `<tr>` tag
2. The tag for normal row items is `<td>`. Add `<td>Text</td>` between the `<tr>` and `</tr>` tags. You will need the same number of `<td></td>` as the number of headings
3. For each `<td>Text</td>` replace Text with what you want to appear in that table cell - a cell is the name for a box in the table.

## Keyboard Shorcuts

1. Items in the menu ususally have a keyboard shortcut next to them. You can press the shortcut to do the same as clicking on the menu.
2. `File->Save`, command s
3. `Edit->Copy`, command c
4. `Edit->Paste`, command v
5. `Edit->Undo`, command z
6. `Edit->Cut`, command x

## Unordered Lists

1. Use `<ul></ul>` for unordered lists. These are lists with bullet points instead of numbers
2. To add an item to the list you add `<li></li>` between the `<ul>` tags. 
3. Whatever you want to put in the list item goes in between the `<li>` tags.

## Ordered Lists

1. Use `<ol></ol>` for unordered lists. These are lists with bullet points instead of numbers
2. To add an item to the list you add `<li></li>` between the `<ol>` tags. 
3. Whatever you want to put in the list item goes in between the `<li>` tags.

## Change color using css classes

1. In the css file create a css class with a name. Inside this class add `color: ` and the name of a color. For example
```css
.my-colored-text {
    color: blue
}
```
2. In the html file whatever you add this classname to will have the color blue. You can change the color to whatever you want.
3. For example to add it to a heading use `<h1 class="my-colored-text">Heading Text</h1>"`
4. For example to add it to a paragraph use `<p class="my-colored-text">blah blah blah<p>`
5. You can also change other things about the text here e.g. you can change the font size by adding `font-size: 36px;` to the css class e.g.
```css
.my-colored-text {
    color: blue;
    font-size: 36px;
}
```

## Change color using li:hover

1. You can change the color of the text if you hover over a list item by using the `li:hover` class. For example
```css
li:hover {
    color: turquoise
}
```
2. This will change the color of the text to turquoise when you hover over it with the mouse.
3. When you move the mouse away, the text will go back to its original color.

## Change color using li:active

1. You can change the color of the text for as long as you click on a list item by using the `li:active` class. For example
```css
li:active {
    color: gray;
}
```
2. This will change the color of the text to gray when you click on it with the mouse.
3. When you stop holding down the mouse button, the text will go back to its original color.

## Link to second webpage

1. To link to a second webpage we use the `<a>` tags.
2. Add `<a href="index2.html">TEXT</a>` to the webpage
3. Replace the index2.html with the address of the website you want to go to
4. Replace the TEXT with the text of the link that you want to show
5. For example to link to youtube you could add `<a href="www.youtube.com">Go To Youtube!!!</a>`

## Website for Presentation

The website will be required to be created by some time in December. It must contain the following items.

### HTML For Presentation
* Required tags - `<html>`, `<body>`, `<head>`
* Headings - `<h1>` .. `<h6>`
* `<p>` * 2
* Link to CSS
* One list
* One Table
* Two `<a href ...` link
* Three images
* One Youtube Embed
### CSS for presentation
* Font Change
* Font Color
* Background Color and image
* Pseudo selectors - `hover` and `active`
