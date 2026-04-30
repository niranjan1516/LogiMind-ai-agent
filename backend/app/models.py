from sqlalchemy import Column, String, Float, DateTime, text
from sqlalchemy.dialects.postgresql import UUID
from .database import Base

class Driver(Base):
    __tablename__ = "drivers"
    
    driver_id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(String(100), nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)
    status = Column(String(20), default="AVAILABLE")
    efficiency_score = Column(Float, default=100.0)
    created_at = Column(DateTime, server_default=text("NOW()"))