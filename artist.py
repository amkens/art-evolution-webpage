import streamlit as st

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="Art.exe",
    page_icon="🎨",
    layout="wide"
)

# ---------------------- HEADER SECTION ----------------------
st.title("🎨 Rebooting the way you see art — past, present, and beyond.")
st.write("Tracing the evolution, economy, and eccentricities of art.")

# ---------------------- TAB LAYOUT ----------------------
tabs = st.tabs([
    "🏠 Home",
    "🏺 Evolution of Art",
    "💰 Art and the Modern Economy",
    "💬 What Is and Isn’t Art",
    "🎭 Fanart as Art",
    "🌟 The Future of Art"
])

# ---------------------- TAB 1: HOME ----------------------
with tabs[0]:
    st.header("🏠 Home / Introduction")
    st.text_area(
        """Art has never been static. It evolves with us. From the first pigments brushed onto cave walls to the digital canvases of today, art reflects the changing values, tools, and emotions of humanity. It documents not only creativity but also how societies think, feel, and express themselves across time.

This webpage explores that transformation tracing how art has adapted through eras, how it intersects with economy and culture, and how debates about what counts as art continue to shape the creative world. From the evolution of tools and techniques to the rise of fanart and digital expression, this is a journey through arts past, present, and future.

Whether you’re an artist, a critic, or simply curious, Art.exe invites you to look deeper — to question, interpret, and rediscover what art truly means in an age where creativity knows no boundaries.""",
        height=150,
        key="home_text"
    )


# ---------------------- TAB 2: EVOLUTION OF ART ----------------------
with tabs[1]:
    st.header("🏺 Evolution of Art")
    st.text_area(
        """🗿 Prehistoric Art Tools

In the Paleolithic era, early humans crafted tools primarily from stone, bone, and wood. These materials were shaped using techniques like flint knapping, where stones were struck to create sharp edges. Such tools were essential for both survival and artistic expression.

Flint Knives & Scrapers: Used for cutting and engraving.
Bone Needles: Crafted from animal bones, these were likely used for sewing hides and possibly for etching.
Pigment Applicators: Early artists employed brushes made from animal hair or plant fibers, and even their own hands, to apply natural pigments like ochre and charcoal onto cave walls.

These rudimentary tools enabled the creation of intricate cave paintings and carvings, showcasing early humans' creativity and symbolic thinking.

🎨 Renaissance Art Tools

The Renaissance marked a period of artistic innovation, with artists developing more refined tools and techniques.

Drawing Tools:
Silverpoint Styluses: Artists like Leonardo da Vinci used silverpoint for detailed sketches.
Chalks & Charcoal: Natural black and red chalks, often held in reed or brass holders, were used for preliminary drawings.
Pens & Inks: Quill pens filled with iron gall ink allowed for precise line work.

Painting Tools:
Brushes: Made from materials like hog bristles for broad strokes and fine details.
Pigments: Artists mixed natural pigments with binders like egg yolk (tempera) or oil to create paints.
Canvas & Wood Panels: Surfaces prepared with gesso to receive the paint.

🖌️ Modern Art Tools

The Industrial Revolution and the 20th century introduced a plethora of new materials and tools, expanding artists' creative possibilities.

Traditional Tools:
Acrylic & Oil Paints: Synthetic and natural pigments mixed with binders for versatile painting.
Brushes & Palette Knives: Used for applying and manipulating paint on various surfaces.
Printmaking Tools: Carving tools for woodcuts and linocuts, and presses for transferring ink onto paper.

Modern Innovations:
Digital Tablets & Styluses: Devices like Wacom tablets paired with software such as Photoshop enable digital painting and illustration.
3D Printers: Allow artists to create sculptures and models from digital designs.
Mixed Media: Incorporating materials like metal, glass, and found objects into artworks.

These tools have democratized art-making, enabling artists to experiment with new forms and reach broader audiences.

🧠 Contemporary Digital Tools

In today's digital age, artists have access to an array of tools that blend technology with traditional techniques.

Digital Art Software:
Adobe Photoshop & Illustrator: Industry-standard programs for digital painting, illustration, and design.
Procreate: A popular app for digital painting on iPads.
Blender: A 3D modeling and animation software used for creating digital sculptures and animations.

Hardware:
Graphics Tablets: Devices like the Wacom Cintiq allow for pressure-sensitive drawing directly onto the screen.
Virtual Reality (VR) Headsets: Platforms like Tilt Brush enable immersive 3D painting experiences.

These tools have revolutionized art creation, offering infinite possibilities for expression and innovation.""",
        height=350,
        key="evolution_text"
    )

    st.write("Upload up to two images for this section:")
    evo_img1 = st.file_uploader("Upload Image 1", type=["png", "jpg", "jpeg"], key="evo_img1")
    evo_img2 = st.file_uploader("Upload Image 2", type=["png", "jpg", "jpeg"], key="evo_img2")

# ---------------------- TAB 3: ART AND ECONOMY ----------------------
with tabs[2]:
    st.header("💰 Art and the Modern Economy")
    st.text_area(
        """Art is not only a cultural or aesthetic expression but also an economic commodity, with value interpreted in multiple ways. It can be bought, sold, and traded like other assets, and high-value paintings, sculptures, and collectibles often appreciate over time, making them attractive investments. For example, works by Old Masters or contemporary artists can sell for millions at auction, reflecting scarcity, cultural significance, and the reputation of the artist. Economists sometimes treat art like a financial asset, with its price influenced by supply, demand, provenance, and market trends.

Art also reflects economic conditions. Studies analyzing large datasets of historical paintings show that the emotional tone of artworks often correlates with economic cycles. Prosperous periods tend to produce more optimistic and vibrant works, while economic downturns often inspire darker, introspective themes. This demonstrates that art functions as both a mirror of and commentary on society’s economic realities.

Beyond being an asset, art drives economic activity by creating jobs and generating revenue. Galleries, museums, auction houses, art fairs, and cultural institutions employ thousands of people, while also contributing to tourism, education, and the broader creative industries. Nonprofit arts organizations similarly impact local and national economies by fostering cultural engagement and community development.

Pricing art is complex and influenced by both market forces and subjective perception. Factors such as an artist’s reputation, the rarity and provenance of a piece, and current trends or speculation all affect its monetary value. Collectors often purchase art as a means of social signaling, with ownership reflecting taste, status, or cultural capital. At the same time, cultural significance and monetary value do not always align; a piece may hold profound cultural or historical importance without commanding a high price, while some commercially successful works may carry less societal weight.

Technology has further transformed the economics of art. Digital platforms, NFTs, and blockchain marketplaces enable artists to sell directly to global audiences, bypassing traditional intermediaries. These developments are redefining ownership, value, and how art interacts with markets, giving rise to new economic models for creative production.

In short, art exists at the intersection of culture and economy. Its monetary value is shaped by scarcity, reputation, and demand, while its cultural significance reflects societal trends, emotions, and priorities. The economy treats art both as an investment and as a mirror of human experience.""",
        height=350,
        key="economy_text"
    )

    st.write("Upload up to two images for this section:")
    econ_img1 = st.file_uploader("Upload Image 1", type=["png", "jpg", "jpeg"], key="econ_img1")
    econ_img2 = st.file_uploader("Upload Image 2", type=["png", "jpg", "jpeg"], key="econ_img2")

# ---------------------- TAB 4: WHAT IS AND ISN’T ART ----------------------
with tabs[3]:
    st.header("💬 What Is and Isn’t Art")
    st.text_area(
        """Art is more than just colors on a canvas or shapes on a page — it’s an expression of thought, skill, and dedication. Many artists spend weeks, months, or even years perfecting their pieces, blending craftsmanship with meaning and emotion. From this perspective, artworks that appear minimal or effortless often draw criticism. Many argue that such works lack the depth, intention, and technical mastery that make art truly resonate — yet they are often showcased in prestigious galleries and sold for extraordinary prices.

On the other hand, supporters of contemporary and conceptual art see things differently. They believe that art doesn’t always have to rely on visible effort or traditional skill — that the idea, message, and context can be just as powerful. A blank canvas, a single stroke, or an unconventional installation can challenge perceptions, provoke thought, and push the boundaries of what society accepts as art.

This ongoing debate reveals how deeply subjective art is. Some value the labor and craftsmanship behind a work, while others celebrate its ability to question norms and redefine meaning. Both perspectives shape how we experience and evaluate creativity today — proving that art, in all its forms, continues to evolve as a reflection of both thought and effort.""",
        height=350,
        key="debate_text"
    )

    st.write("Upload up to two images for this section:")
    debate_img1 = st.file_uploader("Upload Image 1", type=["png", "jpg", "jpeg"], key="debate_img1")
    debate_img2 = st.file_uploader("Upload Image 2", type=["png", "jpg", "jpeg"], key="debate_img2")

# ---------------------- TAB 5: FANART AS ART ----------------------
with tabs[4]:
    st.header("🎭 Fanart as Art")
    st.text_area(
        """Fanart is often misunderstood. While some people dismiss it as “fan obsession” or just imitation, it’s actually a genuine and creative form of artistic expression. For many artists, drawing their favorite musicians, actors, or fictional characters isn’t about copying — it’s about connection. It’s an emotional response to the art, stories, or performances that have inspired us.

As a fanart artist myself, I’ve heard the comments — that fans are “too obsessed” or that drawing real people isn’t “real art.” But fanart, in its truest sense, is gratitude made visible. It’s how we celebrate the artists who move us, how we say “thank you” through color, detail, and emotion. Every line drawn and every expression captured reflects admiration, not obsession.

Fanart also plays a key role in modern visual culture. It bridges the gap between artist and audience, transforming admiration into creativity. In an age where digital media blurs the line between fandom and artistry, fanart represents how deeply art can inspire — and how inspiration can, in turn, become new art.""",
        height=350,
        key="fanart_text"
    )

    st.write("Upload up to two images for this section:")
    fan_img1 = st.file_uploader("Upload Image 1", type=["png", "jpg", "jpeg"], key="fan_img1")
    fan_img2 = st.file_uploader("Upload Image 2", type=["png", "jpg", "jpeg"], key="fan_img2")

# ---------------------- TAB 6: FUTURE OF ART ----------------------
with tabs[5]:
    st.header("🌟 The Future of Art")
    st.text_area(
        """The future of art is being shaped by technology, globalization, and a shift in how we experience creativity. Art is no longer confined to galleries or traditional mediums; it’s expanding into digital spaces, immersive experiences, and collaborative platforms that connect artists and audiences across the world.

Artificial intelligence, virtual reality, and digital tools are redefining what it means to create. AI-generated art challenges ideas of originality and authorship, while VR and AR experiences invite viewers to step inside the artwork. Artists now use software, data, and even code as their brushes — creating interactive pieces that react to movement, sound, or emotion.

At the same time, social media and online platforms have changed who gets to be seen. Artists don’t need to wait for gallery validation anymore — their work can reach millions directly. Fanart communities, digital illustrators, and independent creators now influence trends and redefine what’s considered “mainstream art.”

However, this future also raises important questions. As AI tools become more advanced, how do we define human creativity? Will digital art hold the same emotional depth as something created by hand? And how will art remain meaningful in a world where anyone can generate an image in seconds?

The future of art isn’t about replacing tradition but expanding it. It’s about blending craftsmanship with technology, emotion with innovation. As art evolves, it continues to reflect what it always has — our imagination, our questions, and the ever-changing world we live in.""",
        height=350,
        key="future_text"
    )

    st.write("Upload up to two images for this section:")
    future_img1 = st.file_uploader("Upload Image 1", type=["png", "jpg", "jpeg"], key="future_img1")
    future_img2 = st.file_uploader("Upload Image 2", type=["png", "jpg", "jpeg"], key="future_img2")

