import { Ionicons } from '@expo/vector-icons'
import { Tabs } from 'expo-router'

export default function TabLayout() {
  return (
    <Tabs
      screenOptions={({ route }) => ({
        headerShown: false, // 🔴 Kein Titel oben
        tabBarActiveTintColor: 'tomato',
        tabBarInactiveTintColor: 'gray',
        tabBarIcon: ({ color, size }) => {
          let iconName: keyof typeof Ionicons.glyphMap = 'home'

          if (route.name === 'index') iconName = 'home'
          else if (route.name === 'plan') iconName = 'calendar'
          else if (route.name === 'einstellungen') iconName = 'settings'

          return <Ionicons name={iconName} size={size} color={color} />
        },
      })}
    />
  )
}
