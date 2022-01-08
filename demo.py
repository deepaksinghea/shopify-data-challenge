import streamlit as st
from PIL import Image

i1 = Image.open('cars/Ford.jpeg')
i2 = Image.open('cars/Lambo.jpeg')
i3 = Image.open('cars/Koenigsegg.jpeg')
i4 = Image.open('cars/BMW.jpeg')
i5 = Image.open('cars/Buggati.jpeg')

cars = [i1,i2,i3,i4,i5]
cars_captions = ['Ford Mustang','Lamborghini','Koenigsegg','BMW','Buggati']

p1 = Image.open('places/newyork.jpeg')
p2 = Image.open('places/goldengate.jpeg')
p3 = Image.open('places/paris.jpeg')
p4 = Image.open('places/tajmahal.jpeg')
p5 = Image.open('places/sydneyoh.jpeg')

places = [p1,p2,p3,p4,p5]
places_captions = ['New York','Golden Gate','Paris','Taj Mahal','Sydney Opera House']

s1 = Image.open('soccer/messi.jpeg')
s2 = Image.open('soccer/cr7.jpeg')
s3 = Image.open('soccer/mbappe.jpeg')
s4 = Image.open('soccer/erling.jpeg')
s5 = Image.open('soccer/ggd.jpeg')

soccer = [s1,s2,s3,s4,s5]
soccer_captions = ['Messi','Ronaldo','Mbappe','Haaland','Donnarumma']

st.title("Shopify Image Repository Challenge")

option = st.selectbox(
     'Select Topic for the Images!',
     ('Cars', 'Places','Soccer','All'))

if option == 'Cars':
    st.image(cars , caption = cars_captions)
elif option == 'Places':
    st.image(places, caption = places_captions)
elif option == 'Soccer':
    st.image(soccer, caption=soccer_captions)
elif option == 'All':
    st.image(cars , caption = cars_captions)
    st.image(places, caption = places_captions)
    st.image(soccer, caption=soccer_captions)

st.header("Project By : Deepak Singh")
