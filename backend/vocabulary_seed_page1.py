from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Vocabulary import Vocabulary
from app.models.base import Base


vocabulary_data = [
    {"en": "(to) Listen", "es": "Escuchar"}, {"en": "(to) Look", "es": "Mirar"},
    {"en": "Student", "es": "Estudiante"}, {"en": "Teacher", "es": "profesor"},
    {"en": "Doctor", "es": "Doctor"}, {"en": "Typist", "es": "Mecanógrafo"},
    {"en": "Lawyer", "es": "Abogado"}, {"en": "Mr", "es": "Señor"},
    {"en": "Mrs", "es": "Señora"}, {"en": "Miss", "es": "Señorita"},
    {"en": "Who?", "es": "¿Quien?"}, {"en": "What?", "es": "¿Que?"},
    {"en": "Yes", "es": "Sí"}, {"en": "* College", "es": "Universidad, facultad"},
    {"en": "A", "es": "Un, una"}, {"en": "An", "es": "Un, una"},
    {"en": "(to) Repeat", "es": "Repetir"}, {"en": "Questions", "es": "Preguntas"},
    {"en": "Reading", "es": "Lectura"}, {"en": "(to) Answer", "es": "Responder"},
    {"en": "With", "es": "Con"}, {"en": "Orange", "es": "Naranja"},
    {"en": "Nurse", "es": "Enfermera"}, {"en": "New", "es": "Nuevo"},
    {"en": "Clock", "es": "Reloj de pared"}, {"en": "(to) Change", "es": "Cambiar"},
    {"en": "Window", "es": "Ventana"}, {"en": "Chair", "es": "Silla"},
    {"en": "Red", "es": "Rojo"}, {"en": "Blue", "es": "Azul"},
    {"en": "Brown", "es": "Café"}, {"en": "Yellow", "es": "Amarillo"},
    {"en": "White", "es": "Blanco"}, {"en": "Black", "es": "Negro"},
    {"en": "Pink", "es": "Rosado"}, {"en": "Gray", "es": "Gris"},
    {"en": "This", "es": "Esta (e), (o)"}, {"en": "These", "es": "Estos, estas"},
    {"en": "That", "es": "Eso(a), aquello (a)"}, {"en": "Those", "es": "Esos, esas, aquellos (as)"},
    {"en": "(to) Give", "es": "Dar, regalar"}, {"en": "(to) Want", "es": "Querer, desean"},
    {"en": "(to) Copy", "es": "Copiar"}, {"en": "(to) Write", "es": "Escribir"},
    {"en": "(to) Read", "es": "Leer"}, {"en": "(to) Open", "es": "Abrir"},
    {"en": "(to) Call", "es": "Llamar"}, {"en": "(to) Do", "es": "Hacer"},
    {"en": "(to) Go", "es": "Ir"}, {"en": "(to) Live", "es": "Vivir"},
    {"en": "(to) Have", "es": "Tener"}, {"en": "Young", "es": "Joven"},
    {"en": "Man", "es": "Hombre"}, {"en": "Name", "es": "Nombre"},
    {"en": "Office", "es": "Oficina"}, {"en": "City", "es": "Ciudad"},
    {"en": "By car", "es": "En carro"}, {"en": "Street", "es": "Calle"},
    {"en": "Alone", "es": "Solo(a)"}, {"en": "Family", "es": "Familia"},
    {"en": "People", "es": "Gente, personas"}, {"en": "Room", "es": "Habitación"},
    {"en": "House", "es": "Casa"}, {"en": "Father", "es": "Papa"},
    {"en": "Mother", "es": "Mama"}, {"en": "Brother", "es": "Hermano"},
    {"en": "Sister", "es": "Hermana"}, {"en": "Businessman", "es": "Hombre de negocios"},
    {"en": "Hospital", "es": "Hospital"}, {"en": "Chemistry student", "es": "Estudiante de química"},
    {"en": "Professor", "es": "Profesor (a)"}, {"en": "Fine", "es": "Bien"},
    {"en": "Well", "es": "Bien"}, {"en": "(to) Get home", "es": "Llegar a casa"},
    {"en": "(to) Attend", "es": "Asistir"}, {"en": "(to) Like", "es": "Gustar"},
    {"en": "(to) Take", "es": "Tomar, agarrar"}, {"en": "(to) Drive", "es": "Conducir"},
    {"en": "(to) Count", "es": "Contar"}, {"en": "(to) Arrive", "es": "Llegar"},
    {"en": "(to) Hurry", "es": "Apresurarse"}, {"en": "What time?", "es": "¿A qué hora?"},
    {"en": "At night", "es": "En la noche, por la noche"}, {"en": "Why?", "es": "¿Por qué?"},
    {"en": "Because", "es": "Porque"}, {"en": "So late", "es": "Muy tarde"},
    {"en": "Night school", "es": "Escuela nocturna"}, {"en": "After", "es": "Después"},
    {"en": "Job", "es": "Empleo, trabajo"}, {"en": "Mail clerk", "es": "Dependiente del correo"},
    {"en": "Computer programming", "es": "Programación de computadora"}, {"en": "Accounting", "es": "Contabilidad"},
    {"en": "Both", "es": "Ambos(as)"}, {"en": "(to) Follow", "es": "Seguir"},
    {"en": "(to) Come", "es": "Venir"}, {"en": "(to) Rest", "es": "Descansar"},
    {"en": "(to) Stay home", "es": "Permanecer en casa"}, {"en": "Sentences", "es": "Oraciones"},
    {"en": "Letter", "es": "Carta"}, {"en": "Book", "es": "Libro"},
    {"en": "Notebook", "es": "Cuaderno"}, {"en": "Lesson", "es": "Lección"}
]


async def seed_page_1():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 1)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=1,
                    module_type="vocabulary",
                    subtitle="Basic Vocabulary - Page 1"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 1 already exists with ID: {page.id}")

            existing_stmt = select(Vocabulary).where(Vocabulary.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_vocab = existing_result.scalars().all()
            
            if existing_vocab:
                print(f"Page 1 already has {len(existing_vocab)} vocabulary items. Skipping...")
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
            print(f"Successfully added {len(vocabulary_data)} vocabulary items to Page 1")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_1())