from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Vocabulary import Vocabulary
from app.models.base import Base


vocabulary_data = [
    {"en": "(to)Beat a path", "es": "Abrir paso"},
    {"en": "(to)Get worse", "es": "Empeorar"},
    {"en": "(to)Switch off", "es": "Apagar, desconectar"},
    {"en": "(to)Demand", "es": "Demandar"},
    {"en": "(to)Let", "es": "Permitir, preguntarse"},
    {"en": "(to)Wonder", "es": "Maravillarse, preguntar"},
    {"en": "(to)Fumble", "es": "Buscar a tientas en el bolsillo"},
    {"en": "Atmosphere", "es": "Atmósfera"},
    {"en": "Carbon dioxide", "es": "Dióxido de carbono"},
    {"en": "Primitive", "es": "Primitivo"},
    {"en": "Asteroids", "es": "Asteroides"},
    {"en": "But rather", "es": "Sino(que)"},
    {"en": "Hospitable", "es": "Hospitalario"},
    {"en": "Mining", "es": "Minería"},
    {"en": "Sums", "es": "Sumas"},
    {"en": "Cooperation", "es": "Cooperación"},
    {"en": "Further", "es": "Mas lejano"},
    {"en": "Doubt", "es": "Duda"},
    {"en": "Nimble", "es": "Hábil"},
    {"en": "Immense", "es": "Inmenso"},
    {"en": "(to)Turn", "es": "Doblar calle, convertir"},
    {"en": "(to)Head out", "es": "Dirigirse a"},
    {"en": "(to)Speed up", "es": "Aumentar la velocidad"},
    {"en": "(to)Pull in", "es": "Llegar, tirar de"},
    {"en": "(to)Spot", "es": "Detectar, manchar"},
    {"en": "(to)Get away", "es": "Escapar, huir"},
    {"en": "(to)Slow down", "es": "Disminuir la velocidad"},
    {"en": "(to)Penetrate", "es": "Penetrar"},
    {"en": "(to)Skid", "es": "Patinar"},
    {"en": "(to)Straighten out", "es": "Enderezar(carro)"},
    {"en": "(to)Pull up", "es": "Detenerse"},
    {"en": "(to)Step on", "es": "Pisar"},
    {"en": "(to)Realize", "es": "Darse cuenta de, entender"},
    {"en": "(to)Smash", "es": "Chocar"},
    {"en": "(to)Struggle", "es": "Pelear, luchar"},
    {"en": "(to)Plunge", "es": "Precipitarse, sumergir"},
    {"en": "(to)Get caught", "es": "Ser atrapado"},
    {"en": "(to)Trudge", "es": "Caminar lento y cansado"},
    {"en": "(to)Give a lift", "es": "Dar un raid"},
    {"en": "(to)Lock", "es": "Enllavar"},
    {"en": "(to)Ride up", "es": "Subir(se)"},
    {"en": "Sad", "es": "Triste"},
    {"en": "Silent", "es": "Silenciosa"},
    {"en": "Outskirts", "es": "Afuera, alrededor"},
    {"en": "Fog", "es": "Neblina"},
    {"en": "Mileage", "es": "Millaje"},
    {"en": "Drizzle", "es": "Llovizna"},
    {"en": "Thick", "es": "Grueso"},
    {"en": "Quick", "es": "Rápido"},
    {"en": "Efficient", "es": "Eficiente"},
    {"en": "(to)Turn off", "es": "Doblar, apagar"},
    {"en": "Head lights", "es": "Luces delanteras"},
    {"en": "Cliff", "es": "Precipicio, acantilado"},
    {"en": "Swinging", "es": "Dando la vuelta alrededor"},
    {"en": "Around the car", "es": "Del carro"},
    {"en": "Along side", "es": "Junto a, a lo largo de"},
    {"en": "Crash", "es": "Choque"},
    {"en": "Scream", "es": "Grito"},
    {"en": "Trap", "es": "Trampa"},
    {"en": "(to)Hesitate", "es": "Vacilar"},
    {"en": "(to)Light", "es": "Encender"},
    {"en": "(to)Hate", "es": "Odiar"},
    {"en": "(to)Blame", "es": "Culpar"},
    {"en": "(to)Bend", "es": "Inclinarse"},
    {"en": "(to)Blackmail", "es": "Chantajear"},
    {"en": "(to)Threaten", "es": "Amenazar, acechar"},
    {"en": "(to)Reply", "es": "Contestar"},
    {"en": "(to)Get rid of", "es": "Deshacerse de"},
    {"en": "(to)Point out", "es": "Señalar, indicar"},
    {"en": "(to)Tighten", "es": "Apretar, atrasarse"},
    {"en": "(to)Concern", "es": "Concernir a, preocupar"},
    {"en": "(to)Pull up", "es": "Detenerse, pararse"},
    {"en": "Empty", "es": "Vacío"},
    {"en": "Except", "es": "Excepto"},
    {"en": "Wallet", "es": "Billetera"},
    {"en": "Bank account", "es": "Cuenta bancaria"},
    {"en": "Sign", "es": "Rótulo, letrero"},
    {"en": "Investigator", "es": "Investigador"},
    {"en": "Detective", "es": "Detective"},
    {"en": "Police force", "es": "Fuerza policial"},
    {"en": "Timid", "es": "Tímido"},
    {"en": "Fur coat", "es": "Abrigo de piel"},
    {"en": "Surprise", "es": "Sorpresa"},
    {"en": "Shabby", "es": "Viejo, antiguo"},
    {"en": "Lighter", "es": "Encendedor"},
    {"en": "Jury", "es": "Jurado"},
    {"en": "Guilty", "es": "Culpable"},
    {"en": "Routine", "es": "Rutina"},
    {"en": "Marriage", "es": "Matrimonio"},
    {"en": "Blonde hair", "es": "Pelo rubio"},
    {"en": "Make up", "es": "Maquillaje"},
    {"en": "Gun", "es": "Pistola, revolver"},
    {"en": "Prison", "es": "Prisión"},
    {"en": "Wad", "es": "Fajo, taco"},
    {"en": "Arrangement", "es": "Arreglo"},
    {"en": "Overlook", "es": "Pasar por alto"},
    {"en": "Along with", "es": "Con"},
    {"en": "(to)Cut through", "es": "Acortar camino"},
    {"en": "(to)Cause", "es": "Causar"},
    {"en": "(to)Sink", "es": "Hundirse"},
    {"en": "(to)Burn", "es": "Quemarse)"}
]


async def seed_page_12():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 12)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=12,
                    module_type="vocabulary",
                    subtitle="Basic Vocabulary - Page 12"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 12 already exists with ID: {page.id}")

            existing_stmt = select(Vocabulary).where(Vocabulary.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_vocab = existing_result.scalars().all()
            
            if existing_vocab:
                print(f"Page 12 already has {len(existing_vocab)} vocabulary items. Skipping...")
                print("If you want to re-seed, delete existing records first.")
                return

            for vocab_item in vocabulary_data:
                vocab = Vocabulary(
                    pages_id=page.id,
                    word=vocab_item["en"],
                    meaning=vocab_item["es"]
                )
                session.add(vocab)

            await session.commit()
            print(f"Successfully added {len(vocabulary_data)} vocabulary items to Page 12")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_12())
