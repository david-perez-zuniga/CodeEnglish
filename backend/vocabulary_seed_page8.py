from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Vocabulary import Vocabulary
from app.models.base import Base


vocabulary_data = [
    {"en": "(to) Keep up with", "es": "Mantenerse al tanto de"},
    {"en": "Existence", "es": "Existencia"},
    {"en": "Market center", "es": "Centro de mercado"},
    {"en": "Open air market", "es": "Mercado al aire libre"},
    {"en": "Farmer", "es": "Granjero"},
    {"en": "Crop", "es": "Cosecha"},
    {"en": "Cloth", "es": "Tela"},
    {"en": "Pottery", "es": "Alfarería"},
    {"en": "Stall", "es": "Establecimiento, Puesto"},
    {"en": "Merchant", "es": "Vendedor"},
    {"en": "Merchandise", "es": "Mercadería"},
    {"en": "Throughout", "es": "A través de"},
    {"en": "Jewelry", "es": "Joyas"},
    {"en": "Close", "es": "Cerca"},
    {"en": "Records", "es": "Discos"},
    {"en": "Influence", "es": "Influencia, influenciar"},
    {"en": "At the bottom", "es": "Abajo"},
    {"en": "Accountant", "es": "Contador"},
    {"en": "Engineering", "es": "Ingeniería"},
    {"en": "(to) Define", "es": "Definir"},
    {"en": "(to) Print", "es": "Imprimir"},
    {"en": "(to) Agree", "es": "Acordar"},
    {"en": "(to) Trust", "es": "Confiar"},
    {"en": "(to) Rely on", "es": "Confiar en"},
    {"en": "(to) Increase", "es": "Incrementar"},
    {"en": "(to) Allow", "es": "Permitir"},
    {"en": "(to) Save", "es": "Ahorrar"},
    {"en": "(to) Charge", "es": "Cobrar"},
    {"en": "(to) Sign", "es": "Firmar"},
    {"en": "Medium", "es": "Medio"},
    {"en": "Such as", "es": "Tales como"},
    {"en": "Food", "es": "Comida"},
    {"en": "Goods", "es": "Bienes"},
    {"en": "Seashell", "es": "Concha de mar"},
    {"en": "Gold", "es": "Oro"},
    {"en": "Silver", "es": "Plata"},
    {"en": "Copper", "es": "Cobre"},
    {"en": "Age", "es": "Edad, época"},
    {"en": "Coin", "es": "Moneda"},
    {"en": "Value", "es": "Valor"},
    {"en": "Worth", "es": "Que vale"},
    {"en": "Honest", "es": "Honesto"},
    {"en": "Reliable", "es": "Confiable"},
    {"en": "(to) Accept", "es": "Aceptar"},
    {"en": "Cash", "es": "Efectivo"},
    {"en": "Loan", "es": "Préstamo"},
    {"en": "Credit", "es": "Crédito"},
    {"en": "Everywhere", "es": "En todas partes"},
    {"en": "Handful", "es": "Manojo, puño"},
    {"en": "Bill", "es": "Cuenta, Billete"},
    {"en": "(to) Require", "es": "Requerir, exigir"},
    {"en": "(to) Consider", "es": "Considerar"},
    {"en": "(to) Pull", "es": "Extraer, sacar"},
    {"en": "(to) Generate", "es": "Generar"},
    {"en": "(to) Distribute", "es": "Distribuir"},
    {"en": "(to) Apply", "es": "Aplicar"},
    {"en": "(to) Set", "es": "Poner"},
    {"en": "Furniture", "es": "Mobiliario"},
    {"en": "Department store", "es": "Almacén"},
    {"en": "(to) Provide", "es": "Proveer"},
    {"en": "Roof", "es": "Techo"},
    {"en": "Trend", "es": "Tendencia"},
    {"en": "Toward", "es": "Hacia"},
    {"en": "Butcher", "es": "Carnicero"},
    {"en": "Baker", "es": "Panadero"},
    {"en": "Shopping center", "es": "Centro comercial"},
    {"en": "Feature", "es": "Característica"},
    {"en": "Merchandising", "es": "Mercadeo"},
    {"en": "Wholesale", "es": "Venta al por mayor"},
    {"en": "Retail", "es": "Venta al detalle"},
    {"en": "Available", "es": "Disponible"},
    {"en": "Vital", "es": "Vital"},
    {"en": "Advertisements", "es": "Anuncios"},
    {"en": "Ads", "es": "Anuncios"},
    {"en": "Enormous", "es": "Enorme"},
    {"en": "Salary", "es": "Salario"},
    {"en": "Among", "es": "Entre mas de 2"},
    {"en": "Owner", "es": "Propietario"},
    {"en": "(to) Combine", "es": "Combinar"},
    {"en": "(to) Create", "es": "Crear"},
    {"en": "(to) Cook", "es": "Cocinar"},
    {"en": "(to) Avoid", "es": "Evitar"},
    {"en": "(to) Sail", "es": "Navegar"},
    {"en": "(to) Spring up", "es": "Surgir"},
    {"en": "(to) Get away", "es": "Escapar"},
    {"en": "(to) Scape", "es": "Escapar"},
    {"en": "Modern", "es": "Modernos"},
    {"en": "Means", "es": "Medios"},
    {"en": "Communication", "es": "Comunicación"},
    {"en": "Giant", "es": "Gigante"},
    {"en": "Sunshine", "es": "Rayos solares"},
    {"en": "Reason", "es": "Razón"},
    {"en": "Whatever", "es": "Lo que sea"},
    {"en": "Until", "es": "Hasta"},
    {"en": "Adventure", "es": "Aventura"},
    {"en": "Horse", "es": "Caballo"},
    {"en": "Camel", "es": "Camello"},
    {"en": "On foot", "es": "A pie"},
    {"en": "Painful", "es": "Doloroso, Penoso"},
    {"en": "Roads", "es": "Calles, caminos"}
]


async def seed_page_8():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 8)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=8,
                    module_type="vocabulary",
                    subtitle="Basic Vocabulary - Page 8"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 8 already exists with ID: {page.id}")

            existing_stmt = select(Vocabulary).where(Vocabulary.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_vocab = existing_result.scalars().all()
            
            if existing_vocab:
                print(f"Page 8 already has {len(existing_vocab)} vocabulary items. Skipping...")
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
            print(f"Successfully added {len(vocabulary_data)} vocabulary items to Page 8")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_8())
