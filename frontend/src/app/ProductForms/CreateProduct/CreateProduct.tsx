import { useRef } from "react";
import { CreateProductForm } from "./ProductForm";
import { getFormItemsNames } from "./functions";

export const CreateProduct = () => {
  const form = useRef<HTMLFormElement>(null);

  const handleSubmit = () => {
    const FORM_ITEMS_NAMES = getFormItemsNames();

    type FormItemsNamesType =
      (typeof FORM_ITEMS_NAMES)[keyof typeof FORM_ITEMS_NAMES];
    const data = {
      ...Object.values(FORM_ITEMS_NAMES).flatMap(
        (value: FormItemsNamesType) => ({
          [value]: form.current?.elements[value].value,
        }),
      ),
    };
    console.log(data);
  };
  return <CreateProductForm form={form} handleSubmit={handleSubmit} />;
};
