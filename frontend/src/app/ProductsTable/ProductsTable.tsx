import { Table } from "react-bootstrap";
import { Product } from "./ProductsTableContainer";
export const ProductsTable: React.FC<{ products: Array<Product> }> = ({
  products,
}) => {
  const headers: Array<keyof Product> = ["name", "price"];
  return (
    <Table striped bordered hover>
      <thead>
        <tr>
          {headers.map((header) => (
            <th key={header}>{header}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {products.map((product) => (
          <tr key={product.id}>
            <td onClick={() => alert("will open modal to update info")}>
              {product.name}
            </td>
            <td>R${product.price}</td>
          </tr>
        ))}
      </tbody>
      <caption>This is the products table</caption>
    </Table>
  );
};
