import { useState } from "react";
import { ForwardedRef, RefObject, useRef } from "react";
import { Button, Form } from "react-bootstrap";
import { getFormItemsNames } from "./functions";

export interface ICreateProductForm {
  form: RefObject<HTMLFormElement>;
  handleSubmit: () => void;
}
export interface FORM_ITEMS_NAMES {}
export const CreateProductForm: React.FC<ICreateProductForm> = ({
  form,
  handleSubmit,
}) => {
  const [priceRange, setPriceRange] = useState<number | undefined>(undefined);
  const priorityOptions = [
    { key: "indispensable", label: "Indispensável" },
    { key: "important", label: "Importante" },
    { key: "nice to have", label: "Legal de se ter" },
  ];
  const FORM_ITEMS_NAMES = getFormItemsNames();
  return (
    <Form ref={form} onSubmit={handleSubmit}>
      <Form.Group>
        <Form.Label>Nome do produto</Form.Label>
        <Form.Control name={FORM_ITEMS_NAMES.PRODUCT_NAME} type="text" />
      </Form.Group>
      <Form.Group>
        <Form.Label>Categoria</Form.Label>
        <Form.Select name={FORM_ITEMS_NAMES.CATEGORY}>
          <option>Tecnologia</option>
          <option>Cama, mesa e banho</option>
          <option>Categoria 3</option>
          <option>Categoria 4</option>
        </Form.Select>
      </Form.Group>
      <Form.Group>
        <Form.Label>Chave</Form.Label>
        <Form.Control name={FORM_ITEMS_NAMES.KEY} type="text" />
      </Form.Group>
      <Form.Group>
        <Form.Label>Quão neceesário é</Form.Label>
        <Form.Select name={FORM_ITEMS_NAMES.PRIORITY}>
          {priorityOptions.map((priority) => (
            <option key={priority.key}>{priority.label}</option>
          ))}
        </Form.Select>
      </Form.Group>
      <Form.Group>
        <Form.Label>Preço máximo</Form.Label>
        <Form.Range
          onChange={({ target: { valueAsNumber } }) =>
            setPriceRange(valueAsNumber)
          }
          name={FORM_ITEMS_NAMES.PRICE_RANGE}
          min={0}
          max={20000}
        />
        {priceRange !== undefined && (
          <div>
            R$
            {priceRange}
          </div>
        )}
      </Form.Group>
      <div style={{ display: "flex", justifyContent: "end", marginTop: 16 }}>
        <Button variant="primary" onClick={handleSubmit}>
          Salvar
        </Button>
      </div>
    </Form>
  );
};
