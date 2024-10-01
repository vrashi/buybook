import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Zak Music",
    page_icon="",
)

def main():
    
    
    
    def write_to_csv(name, add_line_1, add_line_2, city, state, zip, phone_number, book_name):
    # Define CSV file path
        csv_file_path = "Customer_Details.csv"

        # Create a DataFrame or load existing
        try:
            df = pd.read_csv(csv_file_path)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["name", "add_line_1", "add_line_2", "city", "state", "ZIP", "phone_number", "book_name"])

        # Add a new row with the submitted values
        new_row = {"name": name, "add_line_1": add_line_1, "add_line_2":add_line_2, "city":city, "state":state, "ZIP":zip, "phone_number":phone_number, "book_name":book_name}
        df = df._append(new_row, ignore_index=True)

        # Write DataFrame to CSV
        df.to_csv(csv_file_path, index=False)

    
    
    
    def aboutauthor():
        
        st.header("About The Author", divider='rainbow')
        
      
        st.image("author.jpeg", width = 300)
        st.title("Michael Phillip Zak, PhD")
        st.write("Mike earned a Bachelor’s degree in music composition and theory from Rosary Hill College, studying under Soterios Vlahoupoulos and graduating magna cum laude. He earned a Master’s degree in music composition at the State University of New York at Buffalo, where he went on to earn his PhD with distinction in music composition under the guidance of Morton Feldman, Lejaren Hiller, Leo Smit and Wlodziemiercz Kotonski. Later, Mike received a Master of Library Science degree in music librarianship from the University at Buffalo. In addition to teaching, Mike has published a theoretical treatise, including articles for 20th Century Music: “The Monotonal Relationship Between the Augmented and Diminished Polytonal Pitch Sets” (1995), “Progression of Polytonal Pitch Sets” (1996), and “Symmetrical Polytonality” (2009). He also composed and published “Starburst,” a piece for three vibraphones and marimba, which placed in the Percussive Arts Society Competition Contest. Mike has had works recorded on the Contemporary Record Society (CRS), including “Starburst,” “Trio” for violin, cello and piano, “Io” for flute, clarinet and piano, and “Jonathan Edwards” for organ, with Marie Zak on Organ. He is an honorary member of CRS and has written reviews of music scores and recordings.")
        st.title("Books")
        st.write("Popular Song Harmony Explained: A Guide to Hearing Chord Vectors (2018)")
        st.write("Musical Chord Symbols and Symmetrical Polytonality: Hidden Harmonic Dimensions (2024)")


    def book1():
        
        st.header("Michael Phillip Zak, PhD", divider='rainbow')
        st.title("Popular Song Harmony Explained: A Guide to Hearing Chord Vectors")
      
        st.image("popular_song_harmony_cover.png", width = 300)
        st.link_button("Buy", "https://buy.stripe.com/eVaaGK4Qr1xW60E000", help=None, type="primary", disabled=False, use_container_width=False)

        st.write("#### What is the point of music theory and the study of harmony?"):
        st.write("It clarifies by ear colorful textures and meaningful tensions that the harmony expresses. By identifying the underlying structures and hidden forces the mind lights up as well as the heart. If you know what to look for, the ear is prepared to find it, and remember it. Finding it repeatedly in unexpected places enriches the entire listening experience.")
        st.write("It provides a path of hearing through the countless relationships of tones in order to make them conscious, and therefore useful to the composer, improviser, arranger, and deep listener.")
        st.write("What are these powerful hidden natural forces that affects virtually every person in such a way? The study of harmony attempt to reveal these forces, and make them visible. To see the underlying structure of nature and the working elements that exist in the hidden dimensions of music can only be a good thing. Can our systems of understanding be limited? That goes without saying. Do they reveal something? Yes, and the musical test is to hear it, which is a reward in itself.")      
     
        st.write("#### Who would benefit from this study:")
        st.write("Anyone involved with chords and chord progressions, including music students, prospective improvisers, arrangers, composers, singers, and serious listeners with an interest in the nuts and bolts of how musical harmony works.")
        st.write("#### What it aims to do:")
        st.write("Provide a framework for hearing the meaning of individual chords as they relate to the overall goal of a progression.")
        with st.expander("#### How to use it:")
            st.write("Every chord in each song example should be spelled with 100% accuracy. This is critical to identifying the active tones and hearing with clarity the harmonic meaning of each. Then, every harmonic function and substitution must be studied and understood by playing and listening to the individual notes in the examples provided. By doing that, occurrences of the chord functions will become increasingly noticeable when hearing music. Please note, these are typical progressions from actual popular songs; these chords and harmonic principles are evident in countless other songs. Rarely is it otherwise.")
            st.write("Instrumentalists can practice these progressions, employing proper voicing, as these are actual progressions from popular songs, and have value beyond their pedagogical utility. Vocalists can determine which chord tones can provide a basis for a harmonizing part. Improvisers can freely invent their own melodies. Composers and arrangers can use the chord functions and progressions provided by the chart of Normal Harmonic Progression for ideas and suggestions on how to substitute or expand chords. Serious listeners and music lovers can increase their musical consciousness and appreciation of all harmonically based music in general, regardless of time period or style.")
            st.write("Every worthwhile endeavor requires repeated application of effort, and every musician (or athlete, scientist, writer, builder, etc.) knows that. The study of harmony will reveal surprising insights, so be patient, and take it one half step at a time.")
        with st.expander("#### The path is easy to outline:"):
            st.write("Spell the chord with perfect accuracy.")
            st.write("Identify the internal parts that give it directional motion.")
            st.write("Play the progression with smooth voice leading.")
            st.write("Listen to the progression and verify the tendency tones by ear.")

        st.image("vectors.png")
        st.write("©2024 Michael Zak All Rights Reserved")
        st.write("Zak Music Publications")
            
        
        
        

    # Define the URL you want to redirect to
        url = "https://buy.stripe.com/eVaaGK4Qr1xW60E000"
        


        # if submit_button:
        #     if name == "Enter full name" or name == "":
        #         st.error("Enter your name")
        #     elif add_line_1 == "Enter address" or add_line_1 == "":
        #         st.error("Enter your address")
        #     elif city == "E.g. Buffalo" or city == "":
        #         st.error("Enter your city")
        #     elif state == "E.g. NY" or state == "":
        #         st.error("Enter your state")
        #     elif zip == "E.g. 14214" or zip == "":
        #         st.error("Enter your ZIP code")
        #     elif phone_number == "Enter with the country code E.g. +1716...." or phone_number == "":
        #         st.error("Enter your phone number")
        #     else:
        #         write_to_csv(name, add_line_1, add_line_2, city, state, zip, phone_number, "Popular Song Harmony Explained")
        #         st.markdown(f"""
        #             <meta http-equiv="refresh" content="0; url={url}">
        #         """, unsafe_allow_html=True)


    def book1frombutton():
        # book1desc = "Most importantly, every chord in each song example should be spelled with 100% accuracy. This is critical to identifying the active tones and hearing with clarity the harmonic meaning of each. Then, every harmonic function and substitution must be studied and understood by playing and listening to the individual notes in the examples provided. By doing that, occurrences of the chord functions will become increasingly noticeable when hearing music. Please note, these are typical progressions from actual popular songs; these chords and harmonic principles are evident in countless other songs. Rarely is it otherwise. Instrumentalists can practice these progressions, employing proper voicing, as these are actual progressions from popular songs, and have value beyond their pedagogical utility. Vocalists can determine which chord tones can provide a basis for a harmonizing part. Improvisers can freely invent their own melodies. Composers and arrangers can use the chord functions and progressions provided by the chart of Normal Harmonic Progression for ideas and suggestions on how to substitute or expand chords. Serious listeners and music lovers can increase their musical consciousness and appreciation of all harmonically based music in general, regardless of time period or style. Every worthwhile endeavor requires repeated application of effort, and every musician (or athlete, scientist, writer, builder, etc.) knows that. The study of harmony will reveal surprising insights, so be patient, and take it one half step at a time."

        # display_book("Popular Song Harmony Explained: A Guide to Hearing Chord Vectors", "popular_song_harmony_cover.png", book1desc)
        # Second Container: Last Week Stats
        # st.header("Michael Phillip Zak", divider='rainbow')
        st.header("Popular Song Harmony Explained: A Guide to Hearing Chord Vectors")
      
        st.image("popular_song_harmony_cover.png", width = 300)
        with st.expander("#### Who would benefit from this study:"):
            st.write("Anyone involved with chords and chord progressions, including music students, prospective improvisers, arrangers, composers, singers, and serious listeners with an interest in the nuts and bolts of how musical harmony works.")
        with st.expander("#### What it aims to do:"):
            st.write("Provide a framework for hearing the meaning of individual chords as they relate to the overall goal of a progression.")
        with st.expander("#### How to use it:"):
            st.write("Every chord in each song example should be spelled with 100% accuracy. This is critical to identifying the active tones and hearing with clarity the harmonic meaning of each. Then, every harmonic function and substitution must be studied and understood by playing and listening to the individual notes in the examples provided. By doing that, occurrences of the chord functions will become increasingly noticeable when hearing music. Please note, these are typical progressions from actual popular songs; these chords and harmonic principles are evident in countless other songs. Rarely is it otherwise.")
            st.write("Instrumentalists can practice these progressions, employing proper voicing, as these are actual progressions from popular songs, and have value beyond their pedagogical utility. Vocalists can determine which chord tones can provide a basis for a harmonizing part. Improvisers can freely invent their own melodies. Composers and arrangers can use the chord functions and progressions provided by the chart of Normal Harmonic Progression for ideas and suggestions on how to substitute or expand chords. Serious listeners and music lovers can increase their musical consciousness and appreciation of all harmonically based music in general, regardless of time period or style.")
            st.write("Every worthwhile endeavor requires repeated application of effort, and every musician (or athlete, scientist, writer, builder, etc.) knows that. The study of harmony will reveal surprising insights, so be patient, and take it one half step at a time.")

        # st.write("### Place The Order - $25.00")

        # with st.form(key='user_form'):
        #     name = st.text_input('Name')
        #     add_line_1 = st.text_input('Address Line 1')
        #     add_line_2 = st.text_input('Address Line 2')
        #     city = st.text_input('City')
        #     state = st.text_input('State')
        #     zip = st.text_input('Zip Code')
        #     phone_number = st.text_input('Phone Number')
        # submit_button = st.button(label='Buy')

    # name = st.text_input("Name*", "Enter full name")
    # add_line_1 = st.text_input("Address line 1*", "Enter address")
    # add_line_2 = st.text_input("Address line 2", "Enter address")
    # city = st.text_input("City*", "E.g. Buffalo")
    # state = st.text_input("State*", "E.g. NY")
    # zip = st.text_input("Zip Code*", "E.g. 14214")
    # phone_number = st.text_input("Phone Number*", "Enter with the country code E.g. +1716....")
    # print(client_name)
    # print(property_id)
    # print(website_name)
        


    # Define the URL you want to redirect to
        
        st.link_button("Buy", "https://buy.stripe.com/eVaaGK4Qr1xW60E000", help=None, type="secondary", disabled=False, use_container_width=False)
        url = "https://buy.stripe.com/test_00geWGc543wXg6s3cc"
        



    def book2():

    
        # Second Container: Last Week Stats
        st.header("Michael Phillip Zak, PhD", divider='rainbow')
        st.title("Musical Chord Symbols and Symmetrical Polytonality: Hidden Harmonic Dimensions")
        st.image("musical_chord_symbols_cover.png", width = 300)
        # with st.expander("#### Main Aim of the Study?"):
        st.link_button("Buy", "https://buy.stripe.com/5kA3ei96H7WkexaeUV", help=None, type="primary", disabled=False, use_container_width=False)

        with st.expander("#### What are the problems of music theory description?"):
            st.write("Explanation is a larger concept than definition. We define the elements, then explain their relationships. Relationships occur in levels of influence, some more fundamental than others. Analysis attempts to explain the levels of relationship.")
            st.write("Describing a multidimensional set of relationships using the linear structure of language is the primary problem of music theory. The whole must be grasped to see the relationship of the parts.")
            st.write("Another problem is that the notational system of seven letter names attached to twelve individual pitches is unwieldy when applied to symmetrical relationships. Having a solid command of enharmonic chord spelling is absolutely essential.")

        st.write("#### Main Aim of the Study:")
        st.write("To become sensitized to the hierarchy of vectors at play within a harmonic musical texture that influence its direction towards a resolution.")
        # with st.expander("#### What is Symmetrical Polytonality?"):
        st.write("#### What is Symmetrical Polytonality?")
        st.write("Symmetrical Polytonality is a harmonic environment in which chord structures arising from symmetrically rich pitch sets/scales suggest several simultaneous tonalities. Multiple simultaneous tonal centers are rather uncommon, as the ear (mind) tries to organize the harmony within the prevailing tonality. Very possible to create, but rare in most music.")
        st.write("Symmetrical polytonal elements are very common, however, providing the necessary directional motion that gives a progression its drive towards or away from that reference/resolution tone. The interacting relationships of suggested possible resolutions, and the actual or implied resolutions are a powerful source of structure and harmonic meaning in a musical creation.")
        # with st.expander("#### Importance of Symmetry"):
        st.write("#### Importance of Symmetry:")
        st.write("Symmetrical harmonic structures are the drive mechanism for tonal harmony. The symmetrical scales and the chords associated with them are also responsible for common non-diatonicism found in music involving the equally tempered chromatic scale. Harmonic symmetries manifest themselves in all styles throughout musical history, and became a primary force upon adoption of the equal tempered tuning system.")
        st.image("symmetry.png", width = 300)

        st.write("#### Chord Pods")
        st.image("pod.png", width = 300)
        st.write("#### Symmsets")
        st.image("symset.png", width = 300)
        st.write("©2024 Michael Zak All Rights Reserved")
        st.write("Zak Music Publications")
        
    

        # st.header("Place The Order - $25.00")

        # with st.form(key='user_form'):
        #     name = st.text_input('Name')
        #     add_line_1 = st.text_input('Address Line 1')
        #     add_line_2 = st.text_input('Address Line 2')
        #     city = st.text_input('City')
        #     state = st.text_input('State')
        #     zip = st.text_input('Zip Code')
        #     phone_number = st.text_input('Phone Number')
        #     submit_button = st.form_submit_button(label='Buy')

    # name = st.text_input("Name*", "Enter full name")
    # add_line_1 = st.text_input("Address line 1*", "Enter address")
    # add_line_2 = st.text_input("Address line 2", "Enter address")
    # city = st.text_input("City*", "E.g. Buffalo")
    # state = st.text_input("State*", "E.g. NY")
    # zip = st.text_input("Zip Code*", "E.g. 14214")
    # phone_number = st.text_input("Phone Number*", "Enter with the country code E.g. +1716....")
    # print(client_name)
    # print(property_id)
    # print(website_name)
        


    # Define the URL you want to redirect to
        
        url = "https://buy.stripe.com/5kA3ei96H7WkexaeUV"


        # if submit_button:
        #     if name == "Enter full name" or name == "":
        #         st.error("Enter your name")
        #     elif add_line_1 == "Enter address" or add_line_1 == "":
        #         st.error("Enter your address")
        #     elif city == "E.g. Buffalo" or city == "":
        #         st.error("Enter your city")
        #     elif state == "E.g. NY" or state == "":
        #         st.error("Enter your state")
        #     elif zip == "E.g. 14214" or zip == "":
        #         st.error("Enter your ZIP code")
        #     elif phone_number == "Enter with the country code E.g. +1716...." or phone_number == "":
        #         st.error("Enter your phone number")
        #     else:
        #         write_to_csv(name, add_line_1, add_line_2, city, state, zip, phone_number, "Musical Chord Symbols and Symmetrical Polytonality")
        #         st.markdown(f"""
        #             <meta http-equiv="refresh" content="0; url={url}">
        #         """, unsafe_allow_html=True)

    def book2frombutton():

    
        # Second Container: Last Week Stats
        # st.header("Michael Phillip Zak", divider='rainbow')
        st.header("Musical Chord Symbols and Symmetrical Polytonality: Hidden Harmonic Dimensions")
        st.image("musical_chord_symbols_cover.png", width = 300)
        with st.expander("#### What is the point of music theory and the study of harmony?"):
            st.write("It clarifies by ear colorful textures and meaningful tensions that the harmony expresses. By identifying the underlying structures and hidden forces the mind lights up as well as the heart. If you know what to look for, the ear is prepared to find it, and remember it. Finding it repeatedly in unexpected places enriches the entire listening experience.")
            st.write("It provides a path of hearing through the countless relationships of tones in order to make them conscious, and therefore useful to the composer, improviser, arranger, and deep listener.")
            st.write("What are these powerful hidden natural forces that affects virtually every person in such a way? The study of harmony attempt to reveal these forces, and make them visible. To see the underlying structure of nature and the working elements that exist in the hidden dimensions of music can only be a good thing. Can our systems of understanding be limited? That goes without saying. Do they reveal something? Yes, and the musical test is to hear it, which is a reward in itself.")
        with st.expander("#### What are the problems of music theory description?"):
            st.write("Explanation is a larger concept than definition. We define the elements, then explain their relationships. Relationships occur in levels of influence, some more fundamental than others. Analysis attempts to explain the levels of relationships.")
            st.write("Describing a multidimensional set of relationships using the linear structure of language is the primary problem of music theory. The whole must be grasped to see the relationship of the parts.")
            st.write("Another problem is that the notational system of seven letter names attached to twelve individual pitches is unwieldy when applied to symmetrical relationships. Having a solid command of enharmonic chord spelling is absolutely essential.")
        with st.expander("#### The path is easy to outline:"):
            st.write("Spell the chord with perfect accuracy.")
            st.write("Identify the internal parts that give it directional motion.")
            st.write("Play the progression with smooth voice leading.")
            st.write("Listen to the progression and verify the tendency tones by ear.")
        
        # st.write("### Place The Order - $25.00")

        # with st.form(key='user_form'):
        #     name = st.text_input('Name')
        #     add_line_1 = st.text_input('Address Line 1')
        #     add_line_2 = st.text_input('Address Line 2')
        #     city = st.text_input('City')
        #     state = st.text_input('State')
        #     zip = st.text_input('Zip Code')
        #     phone_number = st.text_input('Phone Number')
        #     submit_button = st.form_submit_button(label='Buy')

    # name = st.text_input("Name*", "Enter full name")
    # add_line_1 = st.text_input("Address line 1*", "Enter address")
    # add_line_2 = st.text_input("Address line 2", "Enter address")
    # city = st.text_input("City*", "E.g. Buffalo")
    # state = st.text_input("State*", "E.g. NY")
    # zip = st.text_input("Zip Code*", "E.g. 14214")
    # phone_number = st.text_input("Phone Number*", "Enter with the country code E.g. +1716....")
    # print(client_name)
    # print(property_id)
    # print(website_name)
        


    # Define the URL you want to redirect to
        st.link_button("Buy", "https://buy.stripe.com/5kA3ei96H7WkexaeUV", help=None, type="secondary", disabled=False, use_container_width=False)
        
        url = "https://buy.stripe.com/test_00geWGc543wXg6s3cc"


        # if submit_button:
        #     if name == "Enter full name" or name == "":
        #         st.error("Enter your name")
        #     elif add_line_1 == "Enter address" or add_line_1 == "":
        #         st.error("Enter your address")
        #     elif city == "E.g. Buffalo" or city == "":
        #         st.error("Enter your city")
        #     elif state == "E.g. NY" or state == "":
        #         st.error("Enter your state")
        #     elif zip == "E.g. 14214" or zip == "":
        #         st.error("Enter your ZIP code")
        #     elif phone_number == "Enter with the country code E.g. +1716...." or phone_number == "":
        #         st.error("Enter your phone number")
        #     else:
        #         write_to_csv(name, add_line_1, add_line_2, city, state, zip, phone_number, "Musical Chord Symbols and Symmetrical Polytonality")
        #         st.markdown(f"""
        #             <meta http-equiv="refresh" content="0; url={url}">
        #         """, unsafe_allow_html=True)
    


    def buybundle():

    
        # Second Container: Last Week Stats
        st.header("Buy The Bundle", divider='rainbow')
        # st.header("Popular Song Harmony Explained: A Guide to Hearing Chord Vectors")
        # st.image("popular_song_harmony_cover.png", width = 200)
        # st.header("Musical Chord Symbols and Symmetrical Polytonality: Hidden Harmonic Dimensions")
        # st.image("musical_chord_symbols_cover.png", width = 200)

        col1, col2 = st.columns(2)
        with col1:
            #st.header("popular_song_harmony_cover")
            st.image("popular_song_harmony_cover.png")

        with col2:
            #st.header("musical_chord_symbols_cover")
            st.image("musical_chord_symbols_cover.png")

        
         
        # st.header("Place The Order - $40.00")

        # with st.form(key='user_form'):
        #     name = st.text_input('Name')
        #     add_line_1 = st.text_input('Address Line 1')
        #     add_line_2 = st.text_input('Address Line 2')
        #     city = st.text_input('City')
        #     state = st.text_input('State')
        #     zip = st.text_input('Zip Code')
        #     phone_number = st.text_input('Phone Number')
        #     submit_button = st.form_submit_button(label='Buy')

    # name = st.text_input("Name*", "Enter full name")
    # add_line_1 = st.text_input("Address line 1*", "Enter address")
    # add_line_2 = st.text_input("Address line 2", "Enter address")
    # city = st.text_input("City*", "E.g. Buffalo")
    # state = st.text_input("State*", "E.g. NY")
    # zip = st.text_input("Zip Code*", "E.g. 14214")
    # phone_number = st.text_input("Phone Number*", "Enter with the country code E.g. +1716....")
    # print(client_name)
    # print(property_id)
    # print(website_name)
        


    # Define the URL you want to redirect to
        st.link_button("Buy", "https://buy.stripe.com/aEUg144Qr5Ocdt6146", help=None, type="secondary", disabled=False, use_container_width=False)
        url = "https://buy.stripe.com/aEUg144Qr5Ocdt6146"


        # if submit_button:
        #     if name == "Enter full name" or name == "":
        #         st.error("Enter your name")
        #     elif add_line_1 == "Enter address" or add_line_1 == "":
        #         st.error("Enter your address")
        #     elif city == "E.g. Buffalo" or city == "":
        #         st.error("Enter your city")
        #     elif state == "E.g. NY" or state == "":
        #         st.error("Enter your state")
        #     elif zip == "E.g. 14214" or zip == "":
        #         st.error("Enter your ZIP code")
        #     elif phone_number == "Enter with the country code E.g. +1716...." or phone_number == "":
        #         st.error("Enter your phone number")
        #     else:
        #         write_to_csv(name, add_line_1, add_line_2, city, state, zip, phone_number, "Both")
        #         st.markdown(f"""
        #             <meta http-equiv="refresh" content="0; url={url}">
        #         """, unsafe_allow_html=True)

    # Create a button
    # if st.button('Buy query param'):
    #     # Redirect the user
    #     if name == "Enter full name" or name == "":
    #         st.error("Enter your name")
    #     elif add_line_1 == "Enter address" or add_line_1 == "":
    #         st.error("Enter your address")
    #     elif city == "E.g. Buffalo" or city == "":
    #         st.error("Enter your city")
    #     elif state == "E.g. NY" or state == "":
    #         st.error("Enter your state")
    #     elif zip == "E.g. 14214" or zip == "":
    #         st.error("Enter your ZIP code")
    #     elif phone_number == "Enter with the country code E.g. +1716...." or phone_number == "":
    #         st.error("Enter your phone number")
    #     else:
    #         write_to_csv(name, add_line_1, add_line_2, city, state, zip, phone_number)
    #         st.experimental_set_query_params(redirect_url=url)

    # # Check if there is a query parameter for redirection
    # query_params = st.experimental_get_query_params()
    # if 'redirect_url' in query_params:
    #     redirect_url = query_params['redirect_url'][0]
    #     # Execute JavaScript to redirect the user
    #     st.write(f"""
    #         <meta http-equiv="refresh" content="0; url={redirect_url}">
    #     """, unsafe_allow_html=True)


    # st.markdown(
        
    #     """
    #     <a href="https://buy.stripe.com/test_00geWGc543wXg6s3cc" target="_blank">
    #         <button style="background-color: #36454F; border: none; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 8px;">
    #             Buy markdown
    #         </button>
    #     </a>
    #     """,
    #     unsafe_allow_html=True
    # )
            
    # st.sidebar.button("About The Author", key=None, help=None, on_click=aboutauthor(), args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)

    # st.sidebar.title("Books Available")
    # selection = st.sidebar.radio("Go to", ["Popular Song Harmony Explained", "Musical Chord Symbols and Symmetrical Polytonality"])
    

    # # Display the appropriate page based on user selection
    # if selection == "Popular Song Harmony Explained":
    #     book1()
    # elif selection == "Musical Chord Symbols and Symmetrical Polytonality":
    #     book2()
    #else:
     #   aboutauthor()
        
    # page_names_to_funcs = {
    #     "About The Author": aboutauthor,
    #     "Popular Song Harmony Explained": book1,
    #     "Musical Chord Symbols and Symmetrical Polytonality": book2,
    #     "Buy The Bundle": buybundle
    # }

    # st.sidebar.title("Books Available!")
    # book_name = st.sidebar.selectbox("", page_names_to_funcs.keys())
    # page_names_to_funcs[book_name]()

    

    page_names_to_funcs_new = {
        "Symmetrical Polytonality": book2,
        "Popular Song Harmony Explained": book1,
        "Buy The Book Bundle": buybundle,
        "About The Author": aboutauthor
    }

    st.sidebar.title("Music Theory Books Available")
    book_name = st.sidebar.selectbox("", page_names_to_funcs_new.keys())
    page_names_to_funcs_new[book_name]()

   

    
    
    

if __name__ == "__main__":
    main()
