from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Vocabulary import Vocabulary
from app.models.base import Base


vocabulary_data = [
    {"en": "(to) Play", "es": "Tocar un instrumento musical, Cantar"},
    {"en": "(to) Sing", "es": "Cantar"},
    {"en": "(to) Have fun", "es": "Pasar bien"},
    {"en": "Rich", "es": "Rico"},
    {"en": "Fashionable", "es": "De moda"},
    {"en": "Private", "es": "Privado"},
    {"en": "Shop", "es": "Tienda"},
    {"en": "Successful", "es": "Exitoso, Próspero"},
    {"en": "Editor", "es": "Editor(A)"},
    {"en": "Magazine", "es": "Revista"},
    {"en": "Party", "es": "Fiesta"},
    {"en": "View", "es": "Vista"},
    {"en": "Guest", "es": "Invitado"},
    {"en": "Chance", "es": "Oportunidad"},
    {"en": "Possession", "es": "Posesión"},
    {"en": "Freedom", "es": "Libertad"},
    {"en": "Trip", "es": "Viaje"},
    {"en": "In spite of", "es": "A pesar de"},
    {"en": "Article", "es": "Artículo"},
    {"en": "Sales figures", "es": "Estadística de venta"},
    {"en": "Advertising", "es": "Propaganda"},
    {"en": "Song", "es": "Canción"},
    {"en": "(to) Quit", "es": "Dejar de hacer algo"},
    {"en": "(to) Imagine", "es": "Imaginar"},
    {"en": "Sight", "es": "Vista"},
    {"en": "Nowadays", "es": "Hoy en día"},
    {"en": "Construction", "es": "Construcción"},
    {"en": "Quickly", "es": "Rápidamente"},
    {"en": "Highway", "es": "Carretera"},
    {"en": "Under", "es": "Debajo"},
    {"en": "Face", "es": "Cara, afrontar, encarar"},
    {"en": "Crane", "es": "Grúa"},
    {"en": "Loads", "es": "Cargamento"},
    {"en": "Material", "es": "Material"},
    {"en": "Nevertheless", "es": "Sin embargo"},
    {"en": "Strong", "es": "Fuerte"},
    {"en": "Garden", "es": "Jardín"},
    {"en": "Overtime", "es": "Tiempo extra"},
    {"en": "Rod", "es": "Varilla, barra"},
    {"en": "(to) Manufacture", "es": "Manufacturar"},
    {"en": "(to) Employ", "es": "Emplear"},
    {"en": "(to) Make sure", "es": "Asegurarse de"},
    {"en": "(to) Respect", "es": "Respetar"},
    {"en": "(to) Support", "es": "Apoyar, soportar"},
    {"en": "(to) Train", "es": "Entrenar"},
    {"en": "(to) Dream", "es": "Soñar"},
    {"en": "(to) Settle down", "es": "Establecerse"},
    {"en": "Center", "es": "Centro"},
    {"en": "Garment", "es": "Vestuario"},
    {"en": "Thousands", "es": "Miles"},
    {"en": "Suits", "es": "Trajes"},
    {"en": "Article", "es": "Artículos"},
    {"en": "Clothing", "es": "Ropa"},
    {"en": "Rows", "es": "Filas"},
    {"en": "Sewing machine", "es": "Máquina de costura"},
    {"en": "In fact", "es": "En realidad"},
    {"en": "Percent", "es": "Por ciento"},
    {"en": "Supervisor", "es": "Supervisor"},
    {"en": "Daily", "es": "Diario"},
    {"en": "Shy", "es": "Tímido"},
    {"en": "Understanding", "es": "Comprensivo"},
    {"en": "Helpful advice", "es": "Consejo de ayuda"},
    {"en": "Responsibility", "es": "Responsabilidad"},
    {"en": "Out of work", "es": "Sin trabajo"},
    {"en": "Noise", "es": "Ruido"},
    {"en": "Activity", "es": "Actividad"},
    {"en": "(to) Break down", "es": "Descomponerse, Separar"},
    {"en": "(to) Require", "es": "Requerir"},
    {"en": "(to) Depend on", "es": "Depender de"},
    {"en": "(to) Set up", "es": "Montar"},
    {"en": "(to) End up", "es": "Terminar"},
    {"en": "(to) Bring up", "es": "Criar"},
    {"en": "(to) Drop out", "es": "Dejar de asistir"},
    {"en": "(to) Fire", "es": "Despedir, desemplear"},
    {"en": "(to) Run out", "es": "Agotarse, terminarse"},
    {"en": "(to) Hang around", "es": "Frecuentar"},
    {"en": "(to) Share", "es": "Compartir"},
    {"en": "(to) Make friends", "es": "Hacer amigos"},
    {"en": "Lose", "es": "Perder"},
    {"en": "(to) Borrow", "es": "Pedir prestado"},
    {"en": "(to) Draw", "es": "Retirar, dibujar"},
    {"en": "(to) Hang", "es": "Colgar"},
    {"en": "(to) Attract", "es": "Atraer"},
    {"en": "(to) Be able", "es": "Ser capaz"},
    {"en": "Without", "es": "Sin"},
    {"en": "Purpose", "es": "Propósito, objetivo"},
    {"en": "Size", "es": "Tamaño"},
    {"en": "Success", "es": "Éxito"},
    {"en": "Deliveries", "es": "Entregas"},
    {"en": "Pocket", "es": "Bolsillo"},
    {"en": "Nearly", "es": "Casi"},
    {"en": "Lucky", "es": "Con suerte"},
    {"en": "Unemployment", "es": "Desempleo"},
    {"en": "However", "es": "Sin embargo"},
    {"en": "Still", "es": "Aun, todavía"},
    {"en": "Edge", "es": "Orilla"},
    {"en": "Entertainment", "es": "Entretenimiento"},
    {"en": "Movement", "es": "Movimiento"}
]


async def seed_page_6():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 6)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=6,
                    module_type="vocabulary",
                    subtitle="Basic Vocabulary - Page 6"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 6 already exists with ID: {page.id}")

            existing_stmt = select(Vocabulary).where(Vocabulary.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_vocab = existing_result.scalars().all()
            
            if existing_vocab:
                print(f"Page 6 already has {len(existing_vocab)} vocabulary items. Skipping...")
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
            print(f"Successfully added {len(vocabulary_data)} vocabulary items to Page 6")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_6())
