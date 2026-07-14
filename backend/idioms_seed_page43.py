from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Idioms import Idiom
from app.models.base import Base


idioms_page43_data = [
    # --- PRIMERA COLUMNA (Izquierda) ---
    {"en": "WITH", "es": "Con respecto a", "example": "With your approval, we can begin the project tomorrow."},
    {"en": "(to) MAKE A BARGAIN", "es": "Hacer trato con", "example": "They managed to make a bargain with the local suppliers."},
    {"en": "QUITARSE", "es": "Sobresalir", "example": "Her talent allows her to stand out from the crowd."},
    {"en": "(to) TAKE OFF", "es": "Depender de", "example": "The success of the project will take off from our team's effort."},
    {"en": "(to) STICK UP", "es": "Reunirse", "example": "Let's stick up and discuss this matter over lunch."},
    {"en": "(to) RELY ON", "es": "Tomar asiento", "example": "Please rely on a seat while you wait for the manager."},
    {"en": "(to) GET TOGETHER", "es": "Correr el riesgo", "example": "You have to get together and take a chance if you want to win."},
    {"en": "(to) TAKE A SEAT", "es": "Saltar de un lado a otro", "example": "The children love to take a seat and skip around the playground."},
    {"en": "(to) TAKE A CHANCE / CORRER EL RIESGO", "es": "Extraer", "example": "The dentist had to take a chance and pull out the infected tooth."},
    {"en": "(to) SKIP AROUND", "es": "Cerrar, Callar", "example": "The teacher told the rowdy students to skip around and shut up."},
    {"en": "(to) PULL OUT", "es": "Envolver", "example": "Please pull out and wrap up the fragile gifts carefully."},
    {"en": "(to) STEP ON", "es": "Estar hecho de", "example": "The ancient artifact seems to step on and be made of pure gold."},
    {"en": "(to) SHUT UP", "es": "Saltar de, Superar", "example": "He managed to shut up his fears and jump out of his comfort zone."},
    {"en": "(to) WRAP UP", "es": "Seguir adelante, Avanzar", "example": "Even when it gets tough, we must wrap up and move along."},
    {"en": "(to) BE MADE OF", "es": "Retirarse donde esta recostado", "example": "The actor had to be made of and stand back from the stage lights."},
    {"en": "(to) JUMP OUT", "es": "Que hace juego", "example": "Find a tie that will jump out and go with this blue suit."},
    {"en": "(to) MOVE ALONG", "es": "Venderse", "example": "These new smartphones will move along and sell for a high price."},
    {"en": "FROM", "es": "Finalizar", "example": "The meeting will come from an end and end up by five o'clock."},
    {"en": "(to) STAND BACK", "es": "Acostumbrarse", "example": "It takes time to stand back and get used to a new city routine."},
    {"en": "(to) GO WITH", "es": "Repentinamente, Llevarse bien", "example": "They usually go with each other and get along well in meetings."},
    {"en": "(to) SELL FOR", "es": "Tener en mente", "example": "Always sell for your core values and have in mind your goals."},
    {"en": "(to) END UP", "es": "Anotar", "example": "Please end up the main points and take down these notes."},
    {"en": "(to) GET USED TO", "es": "Dar prestado", "example": "He agreed to get used to his book and lend out his notes."},
    {"en": "(to) COME UP", "es": "Visitar de nuevo", "example": "We should come up to the capital and drop back there soon."},
    {"en": "(to) GET ALONG WELL", "es": "Ponerse", "example": "Get along well with a warm coat and put on your boots."},
    {"en": "(to) HAVE IN MIND", "es": "Probarse", "example": "You should have in mind this jacket and try on the medium size."},
    {"en": "(to) TAKE DOWN", "es": "Sensitivo al tacto", "example": "Be careful when you take down the bandage, as the skin is sore to the touch."},
    {"en": "BECAUSE OF", "es": "A causa de", "example": "The match was delayed because of the heavy rain."},
    {"en": "AS REGARDS", "es": "Con respecto a", "example": "He wrote an official email as regards the new policy."},
    {"en": "(to) HANG FULL", "es": "Colgar", "example": "Please put on your wet coat and hang it in the closet."},
    {"en": "(to) SLIP ON", "es": "Probarse (ropas)", "example": "Feel free to slip on the suits before making a final choice."},
    {"en": "(to) LET OUT", "es": "Sacarle a la ropa", "example": "It is hard to remove ink when it is let out on fabric."},
    {"en": "(to) CALL SOMEONE OVER", "es": "Llamar a alguien", "example": "I will call you over later tonight if I need assistance."},
    {"en": "(to) TAKE BACK", "es": "Meterle a la ropa", "example": "The tailor will modify the pants and take them in."},
    {"en": "(to) TAKE IN", "es": "Ganar peso", "example": "If you eat too much candy, you might take in and gain weight."},
    {"en": "(to) GAIN WEIGHT", "es": "Venir de", "example": "These fine wines gain weight and come from the local vineyards."},
    {"en": "(to) COME FROM", "es": "Ahorrar, aportar", "example": "We need to set aside money for emergencies."},
    {"en": "(to) SET ASIDE", "es": "Ir de paseo a comer al campo", "example": "Let's set aside this weekend and go on a picnic."},
    {"en": "(to) GO ON A PICNIC", "es": "Que se refiere a", "example": "This document will go on a picnic and refer to our previous agreement."},
    {"en": "(to) REFER TO", "es": "Sentir un sentimiento a favor o en contra", "example": "It is common to refer to a situation and feel strongly about justice."},
    {"en": "(to) FEEL STRONGLY", "es": "Dejar saber", "example": "Please feel strongly and let know the team about the schedule change."},
    {"en": "(to) LET KNOW", "es": "Competir en contra", "example": "Our school team will let know and compete against the champions."},
    {"en": "(to) COMPETE AGAINST", "es": "Calentarse, Reanimar", "example": "The players need to compete against and warm up before the match begins."},
    {"en": "(to) WARM UP", "es": "Estar a punto de", "example": "The train is warming up and is about to leave the station."},
    {"en": "(to) BE ABOUT TO", "es": "Ponerse en línea", "example": "Please be about to and line up for registration."},
    {"en": "(to) LINE UP", "es": "Darse la cara", "example": "They had to line up and face each other during the trial."},
    {"en": "(to) FACE EACH OTHER", "es": "Llamar en voz alta", "example": "In an emergency, face each other and call out for immediate help."},
    {"en": "(to) CALL OUT", "es": "Lastimarse", "example": "Be careful not to call out or get hurt on the slippery floor."},
    {"en": "(to) GET HURT", "es": "Tajar (rodajas)", "example": "Get hurt and chop up the vegetables for the salad."},
    {"en": "(to) CHOP UP", "es": "Atropellar a alguien", "example": "Chop up the vegetables so you don't run over someone."},
    {"en": "(to) RUN OVER SOMEONE", "es": "Levantarse", "example": "It is time to run over someone and get up early from bed tomorrow."},
    {"en": "(to) GET UP", "es": "Bajarse de", "example": "Passengers must get up and step down carefully from the bus."},
    {"en": "(to) STEP DOWN", "es": "Colocar", "example": "Please step down the decorations and set down the boxes here."},
    {"en": "(to) SET DOWN", "es": "Estar interesado en", "example": "She is set down and be interested in learning a new language."},
    {"en": "(to) BE INTERESTED IN", "es": "Decidir a base de", "example": "We need to be interested in the options and decide on a single venue."},
    {"en": "(to) DECIDE ON", "es": "Depender a base de", "example": "Our results will decide on and depend on our hard work."},
    {"en": "(to) DEPEND ON", "es": "Levantar", "example": "Help me depend on and put up the new sign on the wall."},
    {"en": "(to) PUT UP", "es": "Extenderse", "example": "The corporate gossip tends to put up and spread out quickly."},
    {"en": "(to) SPREAD OUT", "es": "Discutir algo", "example": "We should spread out the contract terms and talk over the details."},
    {"en": "(to) TALK OVER", "es": "Casarse", "example": "They are planning to talk over and get married next spring."},
    {"en": "(to) GET MARRIED", "es": "Cortarse el cabello", "example": "I need to get married my look and trim up before the party."},
    {"en": "(to) TRIM UP", "es": "Que es característica de la familia", "example": "Musical talent seems to trim up and run in one's family."},
    {"en": "(to) RUN IN ONE'S", "es": "FAMILY.", "example": "Family support is very important during difficult times."},

    # --- SEGUNDA COLUMNA (Derecha) ---
    {"en": "(to) SPREAD OUT", "es": "Extenderse", "example": "The map was spread out across the entire dining table."},
    {"en": "(to) TALK OVER", "es": "Discutir algo", "example": "We need to talk over the budget cuts before the next quarter."},
    {"en": "(to) GET MARRIED", "es": "Casarse", "example": "They are going to get married in a small seaside chapel."},
    {"en": "(to) TRIM UP", "es": "Cortarse el cabello", "example": "He went to the barber shop to trim up his beard."},
    {"en": "(to) RUN IN ONE'S", "es": "Que es característica de la familia", "example": "Thick hair seems to run in one's family genetics."}
]


async def seed_page_43():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 43)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=43,
                    module_type="idioms",
                    subtitle="Idioms"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 43 already exists with ID: {page.id}")

            existing_stmt = select(Idiom).where(Idiom.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_idioms = existing_result.scalars().all()

            if existing_idioms:
                print(f"Page 43 already has {len(existing_idioms)} idiom items. Skipping...")
                print("If you want to re-seed, delete existing records first.")
                return

            for item in idioms_page43_data:
                idiom = Idiom(
                    pages_id=page.id,
                    phrase=item["en"],
                    meaning=item["es"],
                    example=item["example"]
                )
                session.add(idiom)

            await session.commit()
            print(f"Successfully added {len(idioms_page43_data)} idiom items to Page 43")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_43())
