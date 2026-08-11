from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Vocabulary import Vocabulary
from app.models.base import Base


vocabulary_data = [
    {"en": "Suddenly", "es": "Repentinamente"},
    {"en": "(to)Cry out", "es": "Exclamar, Gritar"},
    {"en": "(to)Reply", "es": "Contestar, responder"},
    {"en": "(to)Stand", "es": "Soportar"},
    {"en": "(to)Shut down", "es": "Cerrar"},
    {"en": "(to)Suggest", "es": "Sugerir"},
    {"en": "(to)Vote", "es": "Votar"},
    {"en": "(to)Cast", "es": "Echar, depositar, Lanzar"},
    {"en": "(to)Sweep", "es": "Barrer"},
    {"en": "(to)Whirl", "es": "Girar, dar vueltas"},
    {"en": "(to)Spin", "es": "Girar, dar vueltas"},
    {"en": "(to)Hug", "es": "Abrazar"},
    {"en": "(to)Scatter", "es": "Dispersarse"},
    {"en": "(to)Nod", "es": "Hacer señas con la cabeza"},
    {"en": "(to)Flee", "es": "Escapar"},
    {"en": "(to)Equalize", "es": "Igualar"},
    {"en": "Spaceship", "es": "Nave espacial"},
    {"en": "Pirate", "es": "Pirata"},
    {"en": "Galaxy", "es": "Galaxia"},
    {"en": "Earth", "es": "Tierra"},
    {"en": "Alien", "es": "Extranjero, extraterrestrre"},
    {"en": "Length", "es": "Duración"},
    {"en": "Homeless", "es": "Sin hogar"},
    {"en": "Wanderer", "es": "Vagabundo"},
    {"en": "Brain", "es": "Cerebro"},
    {"en": "Trainee", "es": "Aprendiz"},
    {"en": "Computerlike", "es": "Como computadora"},
    {"en": "Capability", "es": "Capacidad"},
    {"en": "Data", "es": "Información"},
    {"en": "Circle", "es": "Círculo"},
    {"en": "Gloomy", "es": "Lóbrego, Melancólico"},
    {"en": "Pressure", "es": "Presión"},
    {"en": "In favor of", "es": "A favor de"},
    {"en": "Against", "es": "En contra de"},
    {"en": "At last", "es": "Por fin"},
    {"en": "Void", "es": "Vacío"},
    {"en": "End over end", "es": "De un lado a otro"},
    {"en": "Powerless", "es": "Sin poder"},
    {"en": "Round and round", "es": "Dando vuelta a la redonda"},
    {"en": "Over and over", "es": "Repentinamente"},
    {"en": "Bright", "es": "Brillante"},
    {"en": "(to)Store", "es": "Almacenar"},
    {"en": "(to)Punch", "es": "Perforar"},
    {"en": "(to)Carry out", "es": "Llevar a cabo"},
    {"en": "(to)Translate", "es": "Traducir, trasladar"},
    {"en": "(to)Announce", "es": "Anunciar"},
    {"en": "(to)Desire", "es": "Desear, anhelar"},
    {"en": "(to)Detail", "es": "Detallar"},
    {"en": "(to)Substract", "es": "Sustraer, restar"},
    {"en": "Natives", "es": "Nativos"},
    {"en": "Smooth", "es": "Suave, Afable, Sin Arrugas"},
    {"en": "Shell", "es": "Concha"},
    {"en": "Message", "es": "Mensaje"},
    {"en": "Knife", "es": "Cuchillo"},
    {"en": "In any case", "es": "En todo caso"},
    {"en": "Unfortunately", "es": "Desafortunadamente"},
    {"en": "Waves", "es": "Olas"},
    {"en": "Canoe", "es": "Canoa"},
    {"en": "Toward", "es": "Hacia"},
    {"en": "Death", "es": "Muerte"},
    {"en": "Safely", "es": "Sin accidente, con cuidado"},
    {"en": "Officer", "es": "Oficial"},
    {"en": "Meanwhile", "es": "Mientras tanto"},
    {"en": "Courageously", "es": "Valientemente"},
    {"en": "Single handedly", "es": "Solo, Sin ayuda"},
    {"en": "Senator", "es": "Senador"},
    {"en": "(to)Install", "es": "Instalar"},
    {"en": "(to)Prove", "es": "Probar"},
    {"en": "(to)Take over", "es": "Hacerse cargo de"},
    {"en": "(to)Store ", "es": "Almacenar"},
    {"en": "(to)Feed", "es": "Alimentar"},
    {"en": "(to)Retrieve", "es": "Dar de vuelta"},
    {"en": "(to)Press", "es": "Apretar"},
    {"en": "(to)File", "es": "archivar"},
    {"en": "(to)Handle", "es": "Manejar, manipular"},
    {"en": "(to)Estimate", "es": "Estimar"},
    {"en": "(to)Figure out", "es": "Descifrar"},
    {"en": "(to)Deposit", "es": "Depositar"},
    {"en": "(to)Withdraw", "es": "Retirar"},
    {"en": "(to)Satisfy", "es": "Satisfacer"},
    {"en": "(to)Monitor", "es": "Comprobar"},
    {"en": "(to)Print", "es": "Imprimir"},
    {"en": "(to)Issue", "es": "Emitir"},
    {"en": "(to)Record", "es": "Registrar, apuntar"},
    {"en": "(to)Spot", "es": "Detectar"},
    {"en": "(to)Work out", "es": "Resolver, solucionar"},
    {"en": "(to)Dial", "es": "Marcar"},
    {"en": "Relatively", "es": "Relativamente"},
    {"en": "Since then", "es": "Desde entonces"},
    {"en": "Purpose", "es": "Propósito, objetivo"},
    {"en": "Master", "es": "Maestro"},
    {"en": "Nightmare", "es": "Pesadilla"},
    {"en": "Mission", "es": "Misión"},
    {"en": "Data ", "es": "Información"},
    {"en": "Bits", "es": "Pedacitos"},
    {"en": "Available", "es": "Disponible"},
    {"en": "Button", "es": "Botón"},
    {"en": "Amount", "es": "Cantidad"},
    {"en": "Old fashioned", "es": "Viejo, antiguo"},
    {"en": "Bookkeeping system", "es": "Sistema de teneduría de libro"}
]


async def seed_page_14():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 14)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=14,
                    module_type="vocabulary",
                    subtitle="Basic Vocabulary - Page 14"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 14 already exists with ID: {page.id}")

            existing_stmt = select(Vocabulary).where(Vocabulary.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_vocab = existing_result.scalars().all()
            
            if existing_vocab:
                print(f"Page 14 already has {len(existing_vocab)} vocabulary items. Skipping...")
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
            print(f"Successfully added {len(vocabulary_data)} vocabulary items to Page 14")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_14())
