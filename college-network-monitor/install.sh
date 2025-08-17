#!/bin/bash
# Setup script
#!/bin/bash

echo "🚀 Setting up College Network Monitor..."

# Install dependencies
sudo apt update
sudo apt install python3-pip snmp -y

# Python requirements
pip install -r requirements.txt

# Update MAC Vendor DB
python3 -c "from mac_vendor_lookup import MacLookup; MacLookup().update_vendors()"

echo "✅ Setup Complete."
