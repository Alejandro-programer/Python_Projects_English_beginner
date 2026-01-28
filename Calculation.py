material = str(input('What type of material is it? CARBON STEEL, STAINLESS, ALUMINUM \n')).strip().upper()
seconds = float(input('How long did the machine take in sec: \n'))

if material == 'CARBON STEEL':
    print('Material: {} \nTotal cost: US${:.2f}'.format(material, 400 * (seconds / 100)))
elif material == 'STAINLESS':
    print('Material: {} \nTotal cost: US${:.2f}'.format(material, 800 * (seconds / 100)))
elif material == 'ALUMINUM':
    print('Material: {} \nTotal cost: US${:.2f}'.format(material, 900 * (seconds / 100)))
