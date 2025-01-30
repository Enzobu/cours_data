#!/bin/bash

options=($(find ./ -type f -name "*.py" | sort))

if [ ${#options[@]} -eq 0 ]; then
  echo "Aucun fichier .py trouvé dans le répertoire courant ou ses sous-dossiers."
  exit 1
fi

echo -e "\n\nVeuillez choisir un numéro dans la liste :"
previous_dir=""
for i in "${!options[@]}"; do
  current_dir=$(dirname "${options[i]}")
  if [ "$current_dir" != "$previous_dir" ]; then
    if [ "$i" -ne 0 ]; then
      echo ""
    fi
    previous_dir="$current_dir"
  fi
  echo "$((i + 1)). ${options[i]}"
done

echo -e "\n"
read -p "Entrez le numéro correspondant à votre choix : " choix
echo -e "\n"

if ! [[ "$choix" =~ ^[0-9]+$ ]] || [ "$choix" -lt 1 ] || [ "$choix" -gt "${#options[@]}" ]; then
  echo "Choix invalide. Veuillez réessayer."
  exit 1
fi

fichier_a_executer="${options[$((choix - 1))]}"

echo -e "Exécution de : $fichier_a_executer\n"
python3 "$fichier_a_executer"
