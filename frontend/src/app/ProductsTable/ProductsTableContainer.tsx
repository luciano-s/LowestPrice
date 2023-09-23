import { ProductsTable } from "./ProductsTable";

export type Product = {
  id: number;
  name: string;
  price: number;
};

export const ProductsTableContainer = () => {
  //request to fetch products
  const products: Product[] = [
    { id: 1, name: "Sofa", price: 3000.0 },
    { id: 2, name: "Guarda roupa", price: 2000.0 },
    { id: 3, name: "Projetor", price: 1000.0 },
    { id: 4, name: "Cama", price: 5000.0 },
    { id: 5, name: "Mesa", price: 1200.0 },
    { id: 6, name: "Estante", price: 650.0 },
  ];
  return <ProductsTable products={products} />;
};
