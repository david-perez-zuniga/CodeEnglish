from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Idioms import Idiom
from app.models.base import Base


idioms_page42_data = [
    {"en": "(to) Take along with", "es": "Llevar consigo", "example": "Don't forget to take your umbrella along with you."},
    {"en": "(to) Strap on", "es": "Colocar y amarrar", "example": "Make sure to strap on your helmet before riding the bike."},
    {"en": "(to) Put in gear", "es": "Poner cualquier cambio", "example": "Put the car in gear and let's go."},
    {"en": "(to) Speed off", "es": "Acelerar", "example": "He got in his car and decided to speed off."},
    {"en": "(to) Hear of", "es": "Tener noticias de", "example": "I have never heard of that software before."},
    {"en": "(to) Get caught", "es": "Ser atrapado", "example": "Don't get caught sleeping during the meeting."},
    {"en": "(to) Take advantage of", "es": "Aprovecharse de", "example": "You should take advantage of this great opportunity."},
    {"en": "(to) Score a run", "es": "Anotar una carrera", "example": "The player managed to score a run in the last inning."},
    {"en": "(to) Hold someone up", "es": "Atrasar", "example": "I don't want to hold you up, so I'll be quick."},
    {"en": "(to) Make someone nervous", "es": "Poner a alguien nervioso", "example": "Speaking in public always makes him nervous."},
    {"en": "(to) Stop off at", "es": "Hacer escala en", "example": "We will stop off at the gas station before leaving the city."},
    {"en": "(to) Be tied", "es": "Estar empatado", "example": "The game is tied 2-2 right now."},
    {"en": "(to) Wind up", "es": "Lanzar la pelota", "example": "He is ready to wind up and throw the ball."},
    {"en": "(to) Hang up", "es": "Colgar", "example": "Please don't hang up the phone."},
    {"en": "(to) Write down", "es": "Anotar", "example": "Let me write down your phone number."},
    {"en": "(to) Call back", "es": "Llamar de nuevo", "example": "I am busy now, I will call back later."},
    {"en": "(to) Get back", "es": "Regresar", "example": "What time did you get back home yesterday?"},
    {"en": "(to) Attendant to", "es": "Atender", "example": "He was attendant to the needs of the guests."},
    {"en": "(to) Step out", "es": "Salir( de un local)", "example": "Mr. Smith just stepped out of the office for a minute."},
    {"en": "(to) Get in touch with", "es": "Comunicarse con", "example": "I need to get in touch with the manager ASAP."},
    {"en": "(to) Put through", "es": "Pasar la llamada", "example": "The receptionist will put you through to the doctor."},
    {"en": "(to) Jot down", "es": "Anotar", "example": "Let me jot down a few notes during the lecture."},
    {"en": "On display", "es": "En exhibición", "example": "The new paintings are on display at the museum."},
    {"en": "Sooner or later", "es": "Tarde o temprano", "example": "Sooner or later, he will find out the truth."},
    {"en": "(to) Bring into", "es": "Reclamar", "example": "They plan to bring new rules into the game."},
    {"en": "(to) Bring out", "es": "Poner en evidencia", "example": "That blue shirt really brings out the color of your eyes."},
    {"en": "(to) Break in", "es": "Amaestrar", "example": "I need to break in these new shoes."},
    {"en": "(to) Break into", "es": "Violentar", "example": "Someone broke into my car last night."},
    {"en": "(to) Put down", "es": "Dominar", "example": "Put down the weapon immediately."},
    {"en": "(to) Pass out", "es": "Desmayarse", "example": "It was so hot that she thought she would pass out."},
    {"en": "(to) Set down", "es": "Poner por escrito", "example": "Please set down your bags on the table."},
    {"en": "(to) Set forth", "es": "Expresar", "example": "He set forth his ideas clearly in the presentation."},
    {"en": "(to) Set out", "es": "Manifestar", "example": "They set out on their journey early in the morning."},
    {"en": "(to) Set to", "es": "Rectificar", "example": "He set to work immediately after arriving."},
    {"en": "(to) Second fiddle", "es": "De menor importancia", "example": "I am tired of playing second fiddle to him."},
    {"en": "(to) Be second to none", "es": "Ser inferior a nadie", "example": "Their customer service is second to none."},
    {"en": "(to) Rush in", "es": "Colarse", "example": "Fools rush in where angels fear to tread."},
    {"en": "(to) Rush out", "es": "Salir de estampida", "example": "Everyone rushed out of the building when the alarm rang."},
    {"en": "(to) Prevail over", "es": "Vencer", "example": "Good will ultimately prevail over evil."},
    {"en": "(to) Prevail upon", "es": "Persuadir", "example": "We tried to prevail upon him to stay for dinner."},
    {"en": "(to) Prey upon", "es": "Devorar", "example": "The lions prey upon weaker animals."},
    {"en": "(to) Pine a way", "es": "Desfallecer", "example": "He seemed to pine away after his dog died."},
    {"en": "(to) Pan out", "es": "Tener \u00e9xito", "example": "We will see how things pan out in the next few weeks."},
    {"en": "Ill bread", "es": "Grosero", "example": "It is ill bread to talk with your mouth full."},
    {"en": "Ill minded", "es": "Mal intencionado", "example": "He is an ill minded person who only wants trouble."},
    {"en": "(to) Go astray", "es": "Descarriarse", "example": "The letter must have gone astray in the mail."},
    {"en": "(to) Go over", "es": "Pasar por encima de", "example": "Let's go over the plan one more time."},
    {"en": "(to) Go under", "es": "Arruinarse", "example": "The company might go under if sales don't improve."},
    {"en": "(to) Give birth to", "es": "Dar a luz", "example": "She is going to give birth to twins."},
    {"en": "(to) Get out of order", "es": "Descomponerse", "example": "The elevator got out of order again today."},
    {"en": "(to) Do over", "es": "Untar, cubrir, Hacer de nuevo", "example": "I made a mistake, so I have to do it over."},
    {"en": "(to) Dash off", "es": "Salir de prisa", "example": "I have to dash off to a meeting now."},
    {"en": "(to) Come through", "es": "Sobrevivir, Superar", "example": "The team really came through in the final quarter."},
    {"en": "(to) Take chance", "es": "Arriesgar", "example": "Sometimes you have to take a chance to succeed."},
    {"en": "(to) Bring forth", "es": "Parir, Dar a luz", "example": "The spring rain will bring forth beautiful flowers."},
    {"en": "(to) Call up", "es": "LLamar por tel\u00e9fono", "example": "I will call up my friend to see if he wants to hang out."},
    {"en": "Little by little", "es": "Poco a poco", "example": "Little by little, she learned to speak the language."},
    {"en": "All day long", "es": "Todo el d\u00eda", "example": "I have been working on this code all day long."},
    {"en": "On purpose", "es": "A prop\u00f3sito", "example": "I didn't break the glass on purpose, it was an accident."},
    {"en": "(to) Wait on", "es": "Servir", "example": "The waitress will wait on your table shortly."},
    {"en": "(to) Take place", "es": "Ocurrir", "example": "The meeting will take place in the main conference room."},
    {"en": "In vain", "es": "En vano", "example": "All his efforts were in vain, he still failed."},
    {"en": "In a hurry", "es": "R\u00e1pidamente", "example": "Sorry, I can't talk right now, I am in a hurry."},
    {"en": "(to) Wake up", "es": "Levantarse de dormir", "example": "I usually wake up at 6 AM every morning."},
    {"en": "Had better", "es": "Ser\u00eda recomendable", "example": "You had better finish your homework before going out."},
    {"en": "Would rather", "es": "Prefer\u00eda", "example": "I would rather stay home than go out in the rain."},
    {"en": "Quite a few", "es": "Mucho, muchas", "example": "There were quite a few people at the concert."},
    {"en": "Day after day", "es": "D\u00eda tras d\u00eda", "example": "He kept practicing the guitar day after day."},
    {"en": "May as well", "es": "Por consiguiente", "example": "Since we are already here, we may as well eat."},
    {"en": "The sooner the better", "es": "Cuanto mas pronto mejor", "example": "Send me the report, the sooner the better."},
    {"en": "For sale", "es": "Para venta", "example": "Is this old bicycle for sale?"},
    {"en": "For rent", "es": "De alquiler", "example": "There is a nice apartment for rent near the university."}
]


async def seed_page_42():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 42)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=42,
                    module_type="idioms",
                    subtitle="Idioms"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 42 already exists with ID: {page.id}")

            existing_stmt = select(Idiom).where(Idiom.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_idioms = existing_result.scalars().all()

            if existing_idioms:
                print(f"Page 42 already has {len(existing_idioms)} idiom items. Skipping...")
                print("If you want to re-seed, delete existing records first.")
                return

            for item in idioms_page42_data:
                idiom = Idiom(
                    pages_id=page.id,
                    phrase=item["en"],
                    meaning=item["es"],
                    example=item["example"]
                )
                session.add(idiom)

            await session.commit()
            print(f"Successfully added {len(idioms_page42_data)} idiom items to Page 42")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_42())
