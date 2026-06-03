from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Idioms import Idiom
from app.models.base import Base


idioms_data = [
    {"en": "(to) Fall in love with", "es": "Enamorarse de", "example": "I think I will fall in love with this city."},
    {"en": "(to) Watch out for", "es": "Tener cuidado de", "example": "Watch out for the broken step."},
    {"en": "(to) Go on", "es": "Continuar", "example": "Please go on with your story, I am listening."},
    {"en": "(to) Tear down", "es": "Demoler", "example": "They will tear down the old building tomorrow."},
    {"en": "(to) Know by sight", "es": "Conocer de vista", "example": "I don't know his name, but I know him by sight."},
    {"en": "(to) Bring up", "es": "Criar", "example": "It is hard to bring up children these days."},
    {"en": "(to) Keep up with", "es": "Mantenerse al tanto", "example": "It is difficult to keep up with the latest technology."},
    {"en": "(to) Think up", "es": "Inventar, descubrir", "example": "We need to think up a new plan."},
    {"en": "(to) Lie down", "es": "Acostarse", "example": "I have a headache, I need to lie down."},
    {"en": "(to) Hold still", "es": "Estarse quieto", "example": "Hold still while I take your picture."},
    {"en": "(to) Take someone by surprise", "es": "Sorprender a alguien", "example": "The sudden rain took us by surprise."},
    {"en": "(to) Come across", "es": "Encontrarse con", "example": "I came across an old book in the attic."},
    {"en": "(to) Cut in", "es": "Interrumpir", "example": "It is rude to cut in when someone is speaking."},
    {"en": "(to) Make room for", "es": "Acomodar", "example": "Can you make room for one more person at the table?"},
    {"en": "(to) Bug one", "es": "Fastidiar, molestar", "example": "Stop humming, it is really bugging me."},
    {"en": "(to) Stand out", "es": "Sobresalir", "example": "Her red dress made her stand out in the crowd."},
    {"en": "(to) Come about", "es": "Suceder, ocurrir", "example": "How did this problem come about?"},
    {"en": "(to) Get on", "es": "Subirse, montarse", "example": "We need to get on the bus right now."},
    {"en": "(to) Get off", "es": "Bajarse", "example": "Let's get off at the next station."},
    {"en": "(to) Turn on", "es": "Encender", "example": "Can you turn on the light?"},
    {"en": "(to) Turn off", "es": "Apagar", "example": "Please turn off the TV before you sleep."},
    {"en": "(to) Put on", "es": "Ponerse( vestuario)", "example": "Put on your coat, it is cold outside."},
    {"en": "(to) Take off", "es": "Quitarse( vestuario)", "example": "Take off your shoes when you enter the house."},
    {"en": "(to) Pick up", "es": "Recoger, zurcir", "example": "Can you pick up those papers from the floor?"},
    {"en": "(to) Call on", "es": "Visitar", "example": "I will call on you tomorrow afternoon."},
    {"en": "(to) Get sick", "es": "Enfermarse", "example": "Dress warmly so you don't get sick."},
    {"en": "(to) Get lost", "es": "Perderse", "example": "Take a map so you don't get lost in the city."},
    {"en": "(to) Hang up", "es": "Colgar", "example": "Don't hang up the phone yet!"},
    {"en": "(to) Leave out", "es": "Omitir", "example": "Do not leave out any details in your report."},
    {"en": "(to) Look over", "es": "Examinar, revisar", "example": "Please look over this document before signing."},
    {"en": "(to) Point out", "es": "Señalar, indicar", "example": "She pointed out the mistakes in my essay."},
    {"en": "(to) Be over", "es": "Haber terminado", "example": "The movie will be over in ten minutes."},
    {"en": "(to) Make out", "es": "Hacer, escribir", "example": "Please make out the check to my name."},
    {"en": "(to) Cash a check", "es": "Hacer efectivo un cheque", "example": "I need to go to the bank to cash a check."},
    {"en": "(to) Take care of", "es": "Cuidarse de", "example": "Who will take care of your dog while you travel?"},
    {"en": "(to) Do business with", "es": "Hacer negocios con", "example": "We do business with several companies in Europe."},
    {"en": "(to) Have need of", "es": "Tener necesidad de", "example": "We have need of more volunteers for the event."},
    {"en": "(to) Be good for", "es": "Ser bueno para", "example": "Eating vegetables is good for your health."},
    {"en": "(to) Look up", "es": "Buscar, indagar", "example": "If you don't know the word, look it up in the dictionary."},
    {"en": "(to) Rip off", "es": "Romper, robar", "example": "That store will try to rip you off with those prices."},
    {"en": "(to) Pick out", "es": "Escoger", "example": "Help me pick out a gift for my sister."},
    {"en": "(to) Get married", "es": "Casarse", "example": "They plan to get married next summer."},
    {"en": "(to) Sell out", "es": "Agotarse( venta)", "example": "The concert tickets will sell out fast."},
    {"en": "(to) Be fond of", "es": "Gustar de", "example": "I am very fond of chocolate ice cream."},
    {"en": "(to) Cut up", "es": "Tajar, cortar enrodajas", "example": "Please cut up the carrots for the soup."},
    {"en": "(to) Get ripe", "es": "madurarse", "example": "These bananas will get ripe in a few days."},
    {"en": "(to) Throw away", "es": "Botar, desechar", "example": "Don't throw away those empty bottles."},
    {"en": "(to) Be allergic to", "es": "Ser alérgico a", "example": "He is allergic to peanuts."},
    {"en": "(to) Be aware of", "es": "Ser consciente de", "example": "You must be aware of the risks involved."},
    {"en": "(to) Come along", "es": "Venir", "example": "Do you want to come along with us to the park?"},
    {"en": "(to) Be acquainted with", "es": "Estar familiarizado con", "example": "I am not acquainted with this software."},
    {"en": "(to) Pass by", "es": "Pasar por", "example": "I pass by your house every morning."},
    {"en": "(to) Find out", "es": "Averiguar", "example": "We need to find out the truth about what happened."},
    {"en": "(to) Speed along", "es": "Aumentar la velocidad", "example": "The car was speeding along the highway."},
    {"en": "(to) Be worried about", "es": "Estar preocupado", "example": "She is worried about her upcoming exam."},
    {"en": "(to) Make up one's mind", "es": "convencer", "example": "He needs to make up his mind about the job offer."},
    {"en": "(to) Change one's mind", "es": "Convencer", "example": "Nothing will make me change my mind."},
    {"en": "(to) Be a matter of", "es": "Ser asunto de", "example": "It is just a matter of time before we win."},
    {"en": "(to) Put off", "es": "Postergar", "example": "Never put off until tomorrow what you can do today."},
    {"en": "(to) Fill something up", "es": "Llenar algo", "example": "Please fill up the gas tank."},
    {"en": "(to) Turn in", "es": "Entregar", "example": "Don't forget to turn in your homework tomorrow."},
    {"en": "(to) Stick to", "es": "Adherir a, sugerir", "example": "Let's stick to the original plan."},
    {"en": "(to) Make good time", "es": "Hacer buen tiempo", "example": "We made good time and arrived early."},
    {"en": "(to) Cut out", "es": "Acortar, recortar", "example": "Cut out the pictures from the magazine."},
    {"en": "(to) Turn over", "es": "Darse vuelta", "example": "If the pancakes are brown, turn them over."},
    {"en": "(to) Wrap around", "es": "Chocar y meterse auna construcción", "example": "He lost control and wrapped his car around a tree."},
    {"en": "(to) Get loose", "es": "Perder el control", "example": "Make sure the dog doesn't get loose."},
    {"en": "(to) Rip through", "es": "Chocar y llevarse todo", "example": "The tornado ripped through the small town."},
    {"en": "(to) Draw up at", "es": "Aproximarse", "example": "The taxi drew up at the front door."},
    {"en": "(to) Get out of", "es": "Salir de", "example": "I want to get out of this boring meeting."}
]


async def seed_page_41():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 41)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=41,
                    module_type="idioms",
                    subtitle="Página 41 - Idioms"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 41 already exists with ID: {page.id}")

            existing_stmt = select(Idiom).where(Idiom.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_idioms = existing_result.scalars().all()

            if existing_idioms:
                print(f"Page 41 already has {len(existing_idioms)} idiom items. Skipping...")
                print("If you want to re-seed, delete existing records first.")
                return

            for item in idioms_data:
                idiom = Idiom(
                    pages_id=page.id,
                    phrase=item["en"],
                    meaning=item["es"],
                    example=item["example"]
                )
                session.add(idiom)

            await session.commit()
            print(f"Successfully added {len(idioms_data)} idiom items to Page 41")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_41())
