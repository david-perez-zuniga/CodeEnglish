from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Idioms import Idiom
from app.models.base import Base


idioms_page44_data = [
    # --- COLUMNA IZQUIERDA ---
    {"en": "(to) Get around something or someone", "es": "Tener el tiempo para hacer...algo, Tener la oportunidad de...", "example": "I hope to get around something or someone like fixing the garage this weekend."},
    {"en": "(to) Fall for something", "es": "Gustarle algo", "example": "Be careful not to fall for something that sounds too good to be true."},
    {"en": "(to) Keep right on", "es": "Continuar", "example": "If you keep right on practicing, your English will improve quickly."},
    {"en": "Right away", "es": "Inmediatamente", "example": "Please call the manager right away because we have an emergency."},
    {"en": "At least", "es": "Al menos, por lo menos", "example": "You should drink at least eight glasses of water every day."},
    {"en": "At last", "es": "Por fin, finalmente", "example": "At last, the train arrived after a long two-hour delay."},
    {"en": "Off and on", "es": "De vez en cuando", "example": "It has been raining off and on throughout the entire afternoon."},
    {"en": "At first", "es": "Primeramente", "example": "At first, the software seemed very complicated to use."},
    {"en": "As usual", "es": "Como de costumbre", "example": "He arrived late as usual, missing the introduction of the speech."},
    {"en": "As always", "es": "Como siempre", "example": "She was helpful as always when I needed technical assistance."},
    {"en": "For good", "es": "Para siempre", "example": "They decided to move to London for good to start a business."},
    {"en": "At times", "es": "A veces", "example": "At times, it is necessary to stop working and take a deep breath."},
    {"en": "By the way", "es": "A propósito", "example": "By the way, did you remember to buy the milk on your way home?"},
    {"en": "By the name of", "es": "Por el nombre de", "example": "A man by the name of Mr. Smith called for you earlier."},
    {"en": "Big deal", "es": "Gran cosa", "example": "Losing that cheap pen is no big deal, so please do not worry."},
    {"en": "Once in a while", "es": "De vez en cuando", "example": "We go out to eat at expensive restaurants once in a while."},
    {"en": "From time to time", "es": "De vez en cuando", "example": "From time to time, she visits her grandparents in the countryside."},
    {"en": "Every so often", "es": "De vez en cuando", "example": "Every so often, the computer system requires a full reboot."},
    {"en": "In a hurry", "es": "Rápidamente", "example": "He packed his suitcase in a hurry because he was late for his flight."},
    {"en": "Nothing further", "es": "Nada adicional", "example": "The detective had nothing further to report about the case."},
    {"en": "Either...or", "es": "O......o", "example": "You can choose either the blue shirt or the red one for the party."},
    {"en": "By mail", "es": "Por correo", "example": "The official documents will be sent to your house by mail."},
    {"en": "No good", "es": "Que no sirve", "example": "This old printer is no good anymore; it just jams the paper."},
    {"en": "As though", "es": "Como si", "example": "He spoke as though he knew everything about modern astronomy."},
    {"en": "On time", "es": "A tiempo", "example": "The meeting started exactly on time, so nobody missed the opening."},
    {"en": "Next to the last", "es": "Penúltimo", "example": "Our team finished in next to the last place during the tournament."},

    # --- COLUMNA DERECHA ---
    {"en": "So far", "es": "Hasta ahora", "example": "So far, we have collected half of the money needed for the trip."},
    {"en": "Bored to death", "es": "Aburrido de muerte", "example": "I was bored to death during the three-hour presentation on tax laws."},
    {"en": "As to", "es": "En cuanto a", "example": "There is no consensus as to which strategy is best for marketing."},
    {"en": "At all", "es": "Del todo", "example": "He did not seem interested in the movie at all and fell asleep."},
    {"en": "Otherwise", "es": "De otro modo", "example": "Hurry up, otherwise you will miss the last bus to the city."},
    {"en": "After all", "es": "Después de todo", "example": "You shouldn't be surprised he won; after all, he practiced daily."},
    {"en": "In addition to", "es": "Además de", "example": "In addition to his salary, he receives a generous yearly bonus."},
    {"en": "On the way back", "es": "Al regreso", "example": "We can stop at the grocery store on the way back from school."},
    {"en": "In advance", "es": "De antemano", "example": "You need to book your hotel tickets in advance during peak season."},
    {"en": "In good shape", "es": "En buena condición", "example": "The classic car is still in good shape despite being fifty years old."},
    {"en": "Nothing to speak of", "es": "Nada de que hablar", "example": "The car suffered minor scratches, but it was nothing to speak of."},
    {"en": "Over there", "es": "Allá", "example": "Your keys are sitting over there on the coffee table by the window."},
    {"en": "On the way", "es": "En camino", "example": "Don't worry, the food delivery is already on the way to your office."},
    {"en": "At bat", "es": "Al bate o a batear", "example": "The crowd cheered loudly when their favorite player was at bat."},
    {"en": "Out to lunch", "es": "Que anda almorzando / fuera", "example": "The secretary is currently out to lunch and will return at two."},
    {"en": "Ready made", "es": "Ya hecho, Confeccionado", "example": "Buying a ready made suit is much faster than getting one tailored."},
    {"en": "On a diet", "es": "A dieta", "example": "She is on a diet, so she skipped the chocolate dessert at dinner."},
    {"en": "Handmade", "es": "Hecho a mano", "example": "This beautiful wooden table was handmade by a local craftsman."},
    {"en": "And so forth", "es": "Etcétera", "example": "They discussed office policies, schedules, budgets, and so forth."},
    {"en": "On the left", "es": "A la izquierda", "example": "The museum entrance will be located on the left side of the street."},
    {"en": "On the way out", "es": "A la salida", "example": "Please drop these garbage bags in the bin on the way out."},
    {"en": "A lot of", "es": "Una gran cantidad de", "example": "There were a lot of people waiting in line outside the theater."},
    {"en": "A great deal of", "es": "Una gran cantidad de", "example": "The new project required a great deal of research and funding."},
    {"en": "Instead of", "es": "En vez de", "example": "Let's walk to the park instead of taking the car this afternoon."},
    {"en": "Prior to", "es": "Antes de", "example": "Prior to signing the contract, make sure you read all the terms."},
    {"en": "In answer to", "es": "En contestación a", "example": "In answer to your email, we are pleased to accept your invitation."},
    {"en": "At night", "es": "De noche", "example": "The streets in this neighborhood are very quiet and peaceful at night."},
    {"en": "As well as", "es": "Así como", "example": "The course covers grammar rules as well as practical conversation."},
    {"en": "Regardless off", "es": "A pesar de", "example": "The event will take place regardless of the bad weather conditions."}
]


async def seed_page_44():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 44)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=44,
                    module_type="idioms",
                    subtitle="Idioms"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 44 already exists with ID: {page.id}")

            existing_stmt = select(Idiom).where(Idiom.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_idioms = existing_result.scalars().all()

            if existing_idioms:
                print(f"Page 44 already has {len(existing_idioms)} idiom items. Skipping...")
                print("If you want to re-seed, delete existing records first.")
                return

            for item in idioms_page44_data:
                idiom = Idiom(
                    pages_id=page.id,
                    phrase=item["en"],
                    meaning=item["es"],
                    example=item["example"]
                )
                session.add(idiom)

            await session.commit()
            print(f"Successfully added {len(idioms_page44_data)} idiom items to Page 44")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_44())
