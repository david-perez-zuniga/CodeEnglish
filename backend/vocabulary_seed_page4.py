from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Vocabulary import Vocabulary
from app.models.base import Base


vocabulary_data = [
    {"en": "Corner", "es": "Esquina"}, {"en": "Uptown", "es": "A fueras de la ciudad"},
    {"en": "Large", "es": "Grande"}, {"en": "Enough", "es": "Suficiente"},
    {"en": "Everybody", "es": "Todo el mundo"}, {"en": "Employee", "es": "Empleado"},
    {"en": "Glad", "es": "Contento, alegre"}, {"en": "Crowded", "es": "Lleno, tumultuoso"},
    {"en": "Cup", "es": "Taza"}, {"en": "Water", "es": "Agua"},
    {"en": "Milk", "es": "Leche"}, {"en": "Glass", "es": "Vaso"},
    {"en": "Bottle", "es": "Botella"}, {"en": "Store", "es": "Tienda"},
    {"en": "Bread", "es": "Pan"}, {"en": "Kitchen", "es": "Cocina"},
    {"en": "Money", "es": "Dinero"}, {"en": "Purse", "es": "Cartera de mujer"},
    {"en": "Truck", "es": "Camión"}, {"en": "Garage", "es": "Garaje, taller"},
    {"en": "Free time", "es": "Tiempo libre"}, {"en": "(to)Get", "es": "Lograr, conseguir"},
    {"en": "(to)Pump", "es": "Bombear"}, {"en": "(to)Check", "es": "Chequear"},
    {"en": "(to)Clean", "es": "Limpiar"}, {"en": "(to)Make", "es": "Hacer"},
    {"en": "(to)Spend", "es": "Emplear el dinero"}, {"en": "(to)Use", "es": "Usar"},
    {"en": "(to)Come back", "es": "Regresar"}, {"en": "(to)Get back", "es": "Regresar"},
    {"en": "Last year", "es": "El año pasado"}, {"en": "Final", "es": "Final"},
    {"en": "Where", "es": "Dónde"}, {"en": "Gas station", "es": "Gasolinera"},
    {"en": "Filling station", "es": "Gasolina"}, {"en": "Gas", "es": "Gasolina"},
    {"en": "What else", "es": "Que más"}, {"en": "Oil", "es": "Aceite"},
    {"en": "Windshield", "es": "Vidrio delantero de carro"}, {"en": "Air", "es": "Aire"},
    {"en": "Tire", "es": "Llanta"}, {"en": "Bank", "es": "Banco"},
    {"en": "Tuition", "es": "Colegiatura"}, {"en": "Wonderful", "es": "Maravilloso"},
    {"en": "That sounds like fun", "es": "Eso suena como alegre"}, {"en": "(to)Walk", "es": "Caminar"},
    {"en": "(to)Major in", "es": "Especializarse en"}, {"en": "(to)Plan", "es": "Planear"},
    {"en": "(to)Teach", "es": "Enseñar, dar clases"}, {"en": "(to)Register", "es": "Matricularse"},
    {"en": "(to)Stand in line", "es": "Permanecer en fila"}, {"en": "(to)Wait", "es": "Esperar"},
    {"en": "(to)Pay", "es": "Pagar"}, {"en": "Uncomfortable", "es": "Incomodo"},
    {"en": "Great", "es": "Grandioso"}, {"en": "Place", "es": "Lugar"},
    {"en": "Cafeteria", "es": "Cafetería"}, {"en": "Low", "es": "Bajo"},
    {"en": "Expensive", "es": "Caro"}, {"en": "Basement", "es": "Sótano"},
    {"en": "(to)Travel", "es": "Viajar"}, {"en": "(to)Leave", "es": "Salir, dejar"},
    {"en": "(to)Catch", "es": "Agarrar, coger"}, {"en": "(to)Meet", "es": "Reunirse, Encontrarse"},
    {"en": "(to)Return", "es": "Regresar"}, {"en": "(to)Discover", "es": "Descubrir"},
    {"en": "(to)Invent", "es": "Inventar"}, {"en": "Sales manager", "es": "Gerente de ventas"},
    {"en": "On business", "es": "De negocios"}, {"en": "Out of town", "es": "Fuera de la ciudad"},
    {"en": "At all", "es": "Del todo"}, {"en": "Airport", "es": "Aeropuerto"},
    {"en": "Then", "es": "Entonces, después"}, {"en": "Airplane", "es": "Avión"},
    {"en": "How long", "es": "Cuánto tiempo"}, {"en": "Sales staff", "es": "Personal de ventas"},
    {"en": "Meetings", "es": "Reuniones"}, {"en": "The same thing", "es": "Lo mismo"},
    {"en": "Until", "es": "Hasta"}, {"en": "Oxygen", "es": "Oxigeno"},
    {"en": "Electric light bulb", "es": "Bombillo eléctrico"}, {"en": "(to)Measure", "es": "Medir"},
    {"en": "Semester", "es": "Semestre"}, {"en": "Again", "es": "De nuevo, otra vez"},
    {"en": "Between", "es": "Entre(dos)"}, {"en": "Parents", "es": "Padres"},
    {"en": "Fast", "es": "Rápido, velóz"}, {"en": "Slow", "es": "Lento"},
    {"en": "Long", "es": "Largo"}, {"en": "Cold", "es": "Frio"},
    {"en": "(to)Learn", "es": "Aprender"}, {"en": "(to)Enjoy", "es": "Disfrutar"}
]


async def seed_page_4():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 4)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=4,
                    module_type="vocabulary",
                    subtitle="Basic Vocabulary - Page 4"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 4 already exists with ID: {page.id}")

            existing_stmt = select(Vocabulary).where(Vocabulary.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_vocab = existing_result.scalars().all()
            
            if existing_vocab:
                print(f"Page 4 already has {len(existing_vocab)} vocabulary items. Skipping...")
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
            print(f"Successfully added {len(vocabulary_data)} vocabulary items to Page 4")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_4())
